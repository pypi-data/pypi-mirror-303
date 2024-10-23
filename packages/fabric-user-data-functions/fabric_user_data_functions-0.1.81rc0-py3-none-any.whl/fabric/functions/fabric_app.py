# flake8: noqa: I005
import queue
import threading
import time
import traceback
from typing import Any, Callable, Dict, List, Optional, Union, \
    Iterable
from azure.functions.decorators.http import HttpTrigger, HttpOutput, \
    HttpMethod
from azure.functions.decorators.core import DataType, \
    AuthLevel, InputBinding
from azure.functions.decorators.utils import parse_singular_param_to_enum, \
    parse_iterable_param_to_enums
from azure.functions import FunctionApp, HttpResponse
from azure.functions.decorators.core import DataType
from pydoc import locate
import json
import azure
import inspect
import logging

from fabric.functions.udf_exception import UserDataFunctionInternalError, UserDataFunctionTimeoutError, UserDataFunctionError, UserThrownError
from fabric.functions.udf_string import UdfString
from .invoke_response import UserDataFunctionInvokeResponse, FormattedError, StatusCode
from .udf_binding import UdfPropertyInput
from .fabric_class import FabricSqlConnection, FabricLakehouseFilesClient, FabricLakehouseClient, UserDataFunctionContext
from .item_binding import FabricItemInput, ItemType
from .user_data_function_context_binding import UserDataFunctionContextInput
from .middleware import INVOCATION_ID_PARAMETER, REQ_PARAMETER
from functools import wraps
from typing import Callable, TypeVar
T = TypeVar('T')

class FabricApp(FunctionApp):

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.function_timeout = 200
        super().__init__(AuthLevel.ANONYMOUS)

    def function(self, name=None):
        @self._configure_function_builder_with_func
        def wrap(fb, user_func):
            # Add HTTP Trigger
            fb.add_trigger(trigger=HttpTrigger(
                        name=REQ_PARAMETER,
                        methods=[HttpMethod.POST],
                        auth_level=AuthLevel.ANONYMOUS,
                        route=name))
            fb.add_binding(binding=HttpOutput(name='$return'))

            # Add Custom UDF Bindings
            sig = inspect.signature(user_func)
            for param in sig.parameters.values():
                if self._is_typeof_fabricitem_input(param.annotation):
                    continue
                if(param.name == REQ_PARAMETER):
                    continue
                if self._is_typeof_userdatafunctioncontext_input(param.annotation):
                    # fb.add_binding(binding=UserDataFunctionContext())
                    continue

                # Add custom bindings
                fb.add_binding(binding=UdfPropertyInput(
                    name=param.name, parameterName=param.name, typeName=param.annotation.__name__)
                )

            return fb
        return wrap

    def _is_typeof_fabricitem_input(self, obj):
        # Check to see if parameter is anything we might return from a fabric binding
        return obj == FabricSqlConnection or obj == FabricLakehouseFilesClient or obj == FabricLakehouseClient
    
    def _is_typeof_userdatafunctioncontext_input(self, obj):
        # Check to see if parameter is anything we might return from a fabric binding
        return obj == UserDataFunctionContext
    
    def _get_cleaned_type_and_wrap_str(self, param):
        if hasattr(param.annotation,'__origin__'): 
            return param.annotation.__origin__
        elif param.annotation == str:
            return UdfString
        else:
            return param.annotation
        
    def _add_timeout(self, func: Callable[..., T]):
        @wraps(func)
        def wrapper(*args, **kwargs):
            q = queue.Queue()

            def handle_timeout():
                time.sleep(self.function_timeout)
                q.put(("timeout", None, None, None))
            
            def func_wrapper(*args, **kwargs):
                try:
                    result = func(*args, **kwargs)
                    q.put(("result", result, None, None))
                except Exception as e:
                    stacktrace = traceback.format_exc()
                    q.put(("result", None, e, stacktrace))
            
            threads = []
            threads.append(threading.Thread(target=handle_timeout))
            threads.append(threading.Thread(target=func_wrapper, args=args, kwargs=kwargs))
            for th in threads:
                th.daemon = True
                th.start()

            first_result_to_finish = q.get() # (type, result, exception)
            if (first_result_to_finish[0] == "timeout"):
                raise UserDataFunctionTimeoutError(self.function_timeout)
            elif (first_result_to_finish[2] != None):
                # log the exception
                self.logger.error(first_result_to_finish[3])
                raise first_result_to_finish[2]
            return first_result_to_finish[1]
        return wrapper
    
    

    def _ensure_http_and_formatted_returntype(self, func: Callable[..., T]):
        def _check_args_for_exceptions(args: tuple, kwargs: dict):
            exceptions = []
            for arg in args:
                if issubclass(type(arg), UserDataFunctionError):
                    exceptions.append(arg)
            for key, value in kwargs.items():
                if issubclass(type(value), UserDataFunctionError):
                    value.properties['parameter_name'] = key
                    exceptions.append(value)
            
            return exceptions
        
        def _ensure_response_is_json_serializable(resp: Any):
            try:
                json.dumps(resp)
                return resp
            except (TypeError, OverflowError):
                return getattr(resp, '__dict__', str(resp))
        
        def _log_and_convert_to_formatted_error(e: Exception):
                ret = FormattedError(getattr(e, "error_code", type(e).__name__), getattr(e, 'message', str(e)), getattr(e, 'properties', {}))
                self.logger.error(f"Error during function invoke: {ret.to_json()}")
                return ret
            
        @wraps(func)
        def wrapper(*args, **kwargs):
            invocationId = kwargs[INVOCATION_ID_PARAMETER]
            del kwargs[INVOCATION_ID_PARAMETER]

            invoke_response = UserDataFunctionInvokeResponse()
            invoke_response.functionName = func.__name__
            invoke_response.invocationId = invocationId

            try:
                input_exceptions = _check_args_for_exceptions(args, kwargs)
                if len(input_exceptions) > 0:
                    invoke_response.status = StatusCode.BAD_REQUEST
                    for exception in input_exceptions:
                        invoke_response.add_error(_log_and_convert_to_formatted_error(exception))
                else:
                    resp = func(*args, **kwargs) # The line that actually invokes the user's function
                    serializable_resp = _ensure_response_is_json_serializable(resp)
                    invoke_response.output = serializable_resp
                    invoke_response.status = StatusCode.SUCCEEDED
            except Exception as e:
                if issubclass(type(e), UserDataFunctionError):
                    invoke_response.add_error(_log_and_convert_to_formatted_error(e))

                    if type(e) is UserDataFunctionTimeoutError:
                        invoke_response.status = StatusCode.TIMEOUT
                    elif issubclass(type(e), UserThrownError): # custom exceptions that the user can throw, or they can use as a base class
                        invoke_response.status = StatusCode.BAD_REQUEST
                    else: # custom exceptions that we  throw
                        invoke_response.status = StatusCode.FAILED
                else:
                    invoke_response.status = StatusCode.FAILED
                    # Put the details into an InternalErrorException to hide other details from the exception
                    error = UserDataFunctionInternalError(properties={'error_type': type(e).__name__, 'error_message': getattr(e, 'message', str(e))})
                    invoke_response.add_error(_log_and_convert_to_formatted_error(error))

            # we need to make a new HttpResponse because there is no way to modify the body of an existing one
            headers = {
                'x-fabric-udf-status': str(invoke_response.status)
            }
            formatted_response = {"status_code": 200, "headers": headers, "mimetype": "text/plain", "charset": "utf-8"}
            return HttpResponse(body=invoke_response.to_json(), status_code=formatted_response['status_code'], headers=formatted_response['headers'], mimetype=formatted_response['mimetype'], charset=formatted_response['charset'])

        return wrapper


    def _configure_function_builder_with_func(self, wrap) -> Callable[..., Any]:   
        def decorator(func):
            sig = inspect.signature(func)

            # Update function parameters to include a request object for validation
            params = []
            params.append(inspect.Parameter('req', inspect.Parameter.POSITIONAL_OR_KEYWORD, annotation=azure.functions.HttpRequest))

            for param in sig.parameters.values():
                if param.name != 'req':
                    params.append(inspect.Parameter(param.name, inspect.Parameter.POSITIONAL_OR_KEYWORD, annotation=self._get_cleaned_type_and_wrap_str(param)))

            sig = sig.replace(parameters=tuple(params)).replace(return_annotation=str)
            func.__signature__ = sig

            annotations = {}
            # Update annotations to ensure it uses the cleaned type
            for param in params:
                annotations[param.name] = param.annotation

            # Update return annotation of func to be HttpResponse
            # We should catch if they don't have a return type during metadata generation, but good to double check here
            if 'return' in func.__annotations__:
                annotations['old_return'] = func.__annotations__['return']
            
            annotations['return'] = HttpResponse

            func.__annotations__ = annotations

            # Add wrapper for function to handle ensure all return values are parsed to HttpResponse
            user_func = self._add_timeout(func)
            user_func = self._ensure_http_and_formatted_returntype(user_func)

            fb = self._validate_type(user_func)
            self._function_builders.append(fb)

            return wrap(fb, user_func)

        return decorator
    # The decorator that will be used to tell the function we want a fabric item
    def fabric_item_input(self,
                        argName,
                        alias: str,
                        item_type: Optional[ItemType] = ItemType.SQL,
                        default_item_name: Optional[str] = None,
                        default_workspace_name: Optional[str] = None,
                        data_type : Optional[DataType] = DataType.STRING,
                        **kwargs) \
            -> Callable[..., Any]:

        @self._configure_function_builder
        def wrap(fb):
                
            fb.add_binding(
                binding=FabricItemInput(
                    name=argName,
                    alias=alias,
                    itemType=item_type,
                    defaultItemName=default_item_name,
                    defaultWorkspaceName=default_workspace_name,
                    data_type=parse_singular_param_to_enum(data_type,
                                                        DataType),
                    **kwargs))
            return fb
        
        return wrap
    
    def user_data_function_context_input(self,
                        argName,
                        **kwargs) \
            -> Callable[..., Any]:

        @self._configure_function_builder
        def wrap(fb):
            fb.add_binding(
                binding=UserDataFunctionContextInput(
                    name=argName,
                    **kwargs))
            return fb
        
        return wrap