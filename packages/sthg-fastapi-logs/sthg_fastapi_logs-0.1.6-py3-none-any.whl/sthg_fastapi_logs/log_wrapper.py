import time
import functools
import traceback
import json
import uuid

from starlette.responses import StreamingResponse
from starlette.concurrency import iterate_in_threadpool
from .enumerate import CodeEnum
from .log_util import local_trace, server_logger, error_logger, access_logger

TOKEN_URL = 'http://192.168.1.243:9103/api/user/userInfoByToken'


def get_process_time(start_time, end_time):
    return '{}ms'.format(round((end_time - start_time) * 1000, 6))


def get_status(response):
    if hasattr(response, 'status_code'):
        print(123123, response.status_code)
        return identify_code(response.status_code)
    return CodeEnum.SUCCESS


def get_trace_id():
    if hasattr(local_trace, 'trace_id'):
        return local_trace.trace_id
    return ''


def get_request_method(request):
    return str(request.url)


def get_ip(request):
    return request.client.host


def get_header(request):
    return dict(request.headers)


async def get_request_params(request):
    print("request", request)
    params = dict(request.query_params) if request.query_params else ""
    if not params:
        byte_body = await request.body()
        params = json.loads(byte_body.decode()) if byte_body else ""
    return params


async def get_response(response):
    # 如果响应是一个 StreamingResponse，我们需要特殊处理
    if isinstance(response, StreamingResponse):
        # 我们需要创建一个新的 StreamingResponse
        # 并且修改它的响应体
        async def new_streaming_response(stream):
            async for chunk in stream:
                # 在这里可以处理每个 chunk，例如记录日志、修改内容等
                print(chunk)  # 打印或者处理 chunk
                yield chunk  # 发送 chunk

        return StreamingResponse(new_streaming_response(response.body_iterator), media_type=response.media_type)
    else:
        # 对于非 StreamingResponse，可以直接修改 response.body
        data = await response.body()
        modified_data = data  # 在这里可以修改数据
        return Response(modified_data, media_type=response.media_type, status_code=response.status_code)
    # return data


def identify_code(code):
    code = int(code)
    ranges = {
        CodeEnum.SUCCESS.value: (199, 207),
        CodeEnum.REEOR.value: (1, 1),
        CodeEnum.PARAM_ERROR.value: (400, 499),
        CodeEnum.INNER_REEOR.value: (500, 10000)
        # 可以添加更多的范围
    }

    for identifier, (start, end) in ranges.items():
        if start <= code <= end:
            return identifier
    # 特殊的 code 处理
    if 0 <= code <= 0:
        return CodeEnum.SUCCESS.value
    print(123123)
    return CodeEnum.SUCCESS.value


def get_response_code(response):
    # 拿到 code
    if response and type(response) == dict:
        code = response.get('code') or response.get('Code') or response.get('CODE')
    else:
        code = None
    # 转换 code
    if code:
        code = identify_code(code)
    else:
        code = CodeEnum.SUCCESS.value
    return code


def get_response_msg(response):
    if response and type(response) == dict:
        msg = response.get('msg') or response.get('message') or response.get('Message')
    else:
        msg = None
    return msg


async def get_access_log_str(request, response, start_time, end_time, code, msg, log_type=None, **access_kwargs):
    try:
        t1 = time.time()
        method = get_request_method(request)
        process_time = get_process_time(start_time, end_time)
        # user_id = await get_user_id(request)
        request_ip = get_ip(request)
        request_header = get_header(request)
        request_data = {"ip": request_ip, "request_header": request_header}
        # TODO
        if response:
            response_body = [chunk async for chunk in response.body_iterator]
            reData = {(b''.join(response_body)).decode()}
            response.body_iterator = iterate_in_threadpool(iter(response_body))
            status = get_status(response)
        else:
            status = 500
            reData = None
        reqParams = await get_request_params(request)
        t2 = time.time()
        logRT = get_process_time(t1, t2)
        msg = str(msg).replace('\n', ' ')
        info_msg = f"""{method}\t {status}\t {code}\t {process_time}\t {logRT}\t - \t  用户访问唯一码\t {request_data} \t {reqParams} \t {reData}\t {msg}"""
        print("info_msg", info_msg)
        access_logger.info(str(info_msg))
    except Exception as e:
        error_logger.error('access log error :{}'.format(str(e)))


async def get_access_error_log(request, error, msg):
    try:
        t1 = time.time()
        method = get_request_method(request)
        # user_id = await get_user_id(request)
        request_ip = get_ip(request)
        request_header = get_header(request)
        reqParams = "await get_request_params(request)"
        t2 = time.time()
        logRT = get_process_time(t1, t2)
        msg = str(msg).replace("\n", "")
        info_msg = f'{method} \t {logRT} \t - \t 用户访问唯一码 \t  ip-{request_ip}, header-{request_header} \t {reqParams} \t {msg} \t {error}'
        error_logger.error(str(info_msg))
    except Exception as e:
        error_logger.error('access log error :{}'.format(str(e)))
        raise e


def get_service_log_str(func, response, start_time, end_time, code, msg, *args, **kwargs):
    try:
        t1 = time.time()
        method = func.__name__
        process_time = get_process_time(start_time, end_time)
        result = response
        t2 = time.time()
        logRT = get_process_time(t1, t2)
        info_msg = f'{method} \t 200 \t {code}\t {msg} \t {process_time} \t {logRT} \t 用户访问唯一码 \t {args}{kwargs} \t {result}'
        server_logger.info(str(info_msg))
    except Exception as e:
        error_logger.error('service log error :{}'.format(str(e)))


"""
"time":请求时间
,"traceId":全链路Id
,"method":访问方法
,"status":http状态码
,"code":业务状态码
,"msg": 返回描述，当异常时，可以把简略堆栈放里面
,"resRT": 响应时长
,"logRT": 日志打印耗时
,"guid": 留空
,"requestId":用户访问唯一码
,"userId": 用户id
,"extObj": 扩展信息：包含用Ip,和请求header
,"reqParams": 请求参数
,"reData": 返回参数
"""
from fastapi import (
    FastAPI,
    Request,
    Response
)


def register_middleware(app: FastAPI):
    @app.middleware("http")
    async def log(request: Request, call_next):
        """
        日志记录
        :param request:
        :param call_next:
        :return:
        """
        client_ip = request.client.host
        start_time = time.time()
        try:
            response: Response = await call_next(request)
            process_time = time.time() - start_time
            msg = get_response_msg(response)
            await get_access_log_str(request, response, start_time, process_time, response.status_code, msg)
        except Exception as e:
            process_time = time.time() - start_time
            msg = str(e)
            response = None
            await get_access_log_str(request, response, start_time, process_time, 500, msg)
            raise e
        return response

    @app.middleware("http")
    async def log_middleware(request: Request, call_next):
        local_trace.trace_id = str(uuid.uuid4().hex)
        local_trace.request = request
        response = await call_next(request)
        return response


# 记录api执行日志
def access_log(**access_kwargs):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            print_res: bool = access_kwargs.get('print_res') if access_kwargs.get('print_res') else False
            print_req: bool = access_kwargs.get('print_req') if access_kwargs.get('print_req') else False
            print('是否打印请求', print_res)
            print('是否打印响应', print_req)
            start_time = time.time()
            try:
                response = func(*args, **kwargs)
                # 获取code
                code = get_response_code(response)
                msg = get_response_msg(response)
            except Exception as e:
                code = None
                msg = traceback.format_exc()
                end_time = time.time()
                request = local_trace.request
                response = 'error'
                await get_access_log_str(request, response, start_time, end_time, code, msg, log_type='error',
                                         **access_kwargs)
                print("error", e)
                raise e
            end_time = time.time()
            request = local_trace.request
            await get_access_log_str(request, response, start_time, end_time, code, msg, **access_kwargs)
            return response

        return wrapper

    return decorator


"""
"time":请求时间
,"traceId":全链路Id
,"method":访问方法
,"status":http状态码
,"code":业务状态码
,"msg": 返回描述，当异常时，可以把简略堆栈放里面
,"resRT": 响应时长
,"logRT": 日志打印耗时
,"reqParams": 请求参数
,"reData": 返回参数
"""


# 记录方法执行日志
def service_log(**access_kwargs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            code = None
            msg = None
            response = {}
            start_time = time.time()
            try:
                response = func(*args, **kwargs)
                if isinstance(response, dict):
                    code = str(response.get('code'))
                    msg = response.get('msg') or response.get('message')
            except:
                msg = traceback.format_exc()
            end_time = time.time()
            get_service_log_str(func, response, start_time, end_time, code, msg, *args, **kwargs)
            return response

        return wrapper

    return decorator


def class_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        code = None
        msg = None
        response = {}
        start_time = time.time()
        try:
            response = func(*args, **kwargs)
            if isinstance(response, dict):
                code = get_response_code(response)
                msg = get_response_msg(response)
        except:
            msg = traceback.format_exc()
        end_time = time.time()
        get_service_log_str(func, response, start_time, end_time, code, msg, *args, **kwargs)
        return response

    return wrapper


def class_log(cls):
    for name, method in vars(cls).items():
        if callable(method):
            setattr(cls, name, class_decorator(method))
    return cls
