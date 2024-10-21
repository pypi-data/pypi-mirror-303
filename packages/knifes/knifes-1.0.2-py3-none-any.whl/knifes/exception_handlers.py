from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY


async def http_exception_handler(_request, exc: HTTPException):
    """Register it for Starlette's HTTPException. This way, if any part of Starlette's internal code,
    or a Starlette extension or plug-in, raises a Starlette HTTPException, your handler will be able to catch and handle it."""
    headers = getattr(exc, "headers", None)
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.detail,
        },
        headers=headers,
    )


async def validation_error_handler(_request, exc: RequestValidationError):
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "message": "Request Validation Error",
            "detail": jsonable_encoder(exc.errors()),
        },
    )


def install_exception_handlers(app: FastAPI):
    app.exception_handler(HTTPException)(http_exception_handler)
    app.exception_handler(RequestValidationError)(validation_error_handler)
