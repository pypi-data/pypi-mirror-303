#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：LiShun
@File    ：exception.py
@Time    ：2022/7/12 18:56
@Desc    ：
"""
__all__ = [
    'BaseHTTPException', 'register_exception'
]

import traceback
from typing import Any, Optional, Dict

from fastapi import FastAPI
from fastapi import Request
from fastapi.exceptions import HTTPException, RequestValidationError
from tortoise.validators import ValidationError
from fastapi.responses import JSONResponse, Response

# from base_code.response import json_response
from .base_code.code import CODE
from .log_wrapper import get_access_error_log


def json_response(data=None, message=None, code=200, status_code=200) -> Response:
    code_dict = CODE.get(code) or CODE[400]
    return JSONResponse(
        status_code=status_code,
        content={
            "code": code_dict["code"],
            "message": message or code_dict["zh-cn"],
            "data": data
        }
    )


class BaseHTTPException(HTTPException):
    EXC_STATUS_CODE = 500
    EXC_CODE = 1000
    EXC_MESSAGE = None

    def __init__(
            self,
            message: Any = None,
            status_code: int = 500,
            code: int = 40000,
            headers: Optional[Dict[str, Any]] = None
    ) -> None:
        self.message = message or self.EXC_MESSAGE
        self.status_code = status_code or self.EXC_STATUS_CODE
        self.code = code or self.EXC_CODE
        self.headers = headers

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}(status_code={self.status_code!r}, message={self.message!r})"


def register_exception(app: FastAPI):
    """
    捕获FastApi异常
    :param app:
    :return:
    """

    @app.exception_handler(Exception)
    async def exception_handle(request: Request, exc: Exception):
        msg = traceback.format_exc()
        await get_access_error_log(request, error=str(exc), msg=msg)
        return json_response(code=400, message=str(exc), status_code=200)

    @app.exception_handler(HTTPException)
    async def http_exception_handle(request: Request, exc: HTTPException):
        msg = traceback.format_exc()
        await get_access_error_log(request, error=str(exc), msg=msg)
        return json_response(code=500, message=str(exc.detail), status_code=exc.status_code)

    @app.exception_handler(BaseHTTPException)
    async def base_http_exception_handle(request: Request, exc: BaseHTTPException):
        msg = traceback.format_exc()
        await get_access_error_log(request, error=str(exc), msg=exc)
        return json_response(code=500, message=str(exc.message), status_code=exc.status_code)

    @app.exception_handler(AssertionError)
    async def assert_exception_handle(request: Request, exc: AssertionError):
        exc_str = ''.join(exc.args)
        msg = traceback.format_exc()
        await get_access_error_log(request, error=f"assert_exception > {exc_str}", msg=msg)
        return json_response(code=500, message=exc_str, status_code=500)

    @app.exception_handler(ValidationError)
    async def validation_exception_handle(request: Request, exc: ValidationError):
        exc_str = '|'.join(exc.args)
        msg = traceback.format_exc()
        await get_access_error_log(request, error=f"validation_exception > {exc_str}", msg=msg)
        return json_response(code=500, message=exc_str, status_code=401)

    @app.exception_handler(RequestValidationError)
    async def request_exception_handler(request: Request, exc: RequestValidationError):
        exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
        msg = traceback.format_exc()
        await get_access_error_log(request, error=f"request_exception > {exc_str}", msg=msg)
        return json_response(code=500, message=exc_str, status_code=500)


# 自定义异常类
class TableNameError(Exception):
    __doc__ = "数据库表名命名规则验证错误"


class ColumnNameError(Exception):
    __doc__ = "数据库表属性命名规则验证错误"


class RepetitiveError(Exception):
    __doc__ = "数据库表字段重复错误"


class DataNotFoundError(Exception):
    __doc__ = "数据库数据未找到"


class ParamLackError(Exception):
    __doc__ = "缺少参数"


class ParamValidatedError(Exception):
    __doc__ = "自定义参数格式不正确"


class AlreadyExistsError(Exception):
    __doc__ = "资源已存在"


class CustomRaiseError(Exception):
    __doc__ = "封装自定义报错"
    """
    使用框架自动捕获异常时候使用
    use:
        raise CustomRaiseError(*e.args, int)
    params:
        *e.args: 原始的错误信息
        int: 想要的业务报错信息code
    """
