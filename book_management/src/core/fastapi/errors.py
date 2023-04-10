#
# FastAPI의 기본 에러 핸들러 수정
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2023/04/079 15:24 created.
# @license     Please refer to the LICENSE file on a root directory of project.
#


from typing import Union

from fastapi import status, Request, FastAPI
from fastapi.exceptions import RequestValidationError, StarletteHTTPException
from fastapi.responses import PlainTextResponse

from src.core.fastapi.responses import ORJSONResponse


def init_error_handler(app: FastAPI, admin_email: str):
    @app.exception_handler(Exception)
    async def internal_server_error_handle(
            req: Request,
            exc: Exception,
    ) -> ORJSONResponse:
        return ORJSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                'title': type(exc).__name__,
                'description': str(exc) + ', Contact me ({})'.format(admin_email)
            }
        )

    @app.exception_handler(RequestValidationError)
    async def request_exception_handle(
            req: Request,
            exc: RequestValidationError,
    ) -> ORJSONResponse:
        return ORJSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                'title': 'invalid:data',
                'description': 'wrong value',
                'extra': exc.errors()
            }
        )

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handle(
            req: Request,
            exc: StarletteHTTPException,
    ) -> Union[ORJSONResponse, PlainTextResponse]:
        if exc.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
            return await internal_server_error_handle(req, exc)

        return PlainTextResponse(status_code=exc.status_code)
