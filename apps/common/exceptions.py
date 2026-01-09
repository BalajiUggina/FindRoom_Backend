class AppException(Exception):
    status_code = 400
    message = "Application error"

    def __init__(self, message=None):
        if message:
            self.message = message
        super().__init__(self.message)


class PermissionDenied(AppException):
    status_code = 403
    message = "Permission denied"


class NotFound(AppException):
    status_code = 404
    message = "Resource not found"


class ValidationError(AppException):
    status_code = 400
    message = "Invalid input"


