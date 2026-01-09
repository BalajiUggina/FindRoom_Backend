import logging
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from .exceptions import AppException

logger = logging.getLogger("apps.common")


def custom_exception_handler(exc, context):
    # Handle our custom exceptions
    if isinstance(exc, AppException):
        logger.warning(
            f"{exc.__class__.__name__}: {exc.message}"
        )
        return Response(
            {
                "success": False,
                "error": exc.message,
            },
            status=exc.status_code,
        )

    # Let DRF handle known exceptions (auth, permission, etc.)
    response = exception_handler(exc, context)

    if response is not None:
        logger.error(
            f"DRF Exception: {response.data}",
            exc_info=True,
        )
        return Response(
            {
                "success": False,
                "error": response.data,
            },
            status=response.status_code,
        )

    # Unhandled / unexpected errors (500)
    logger.critical("Unhandled exception", exc_info=True)

    return Response(
        {
            "success": False,
            "error": "Internal server error",
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
