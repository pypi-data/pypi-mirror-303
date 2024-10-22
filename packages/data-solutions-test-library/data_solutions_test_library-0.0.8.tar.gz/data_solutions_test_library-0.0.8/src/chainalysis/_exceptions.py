class DataSolutionsSDKException(Exception):
    """Base class for SDK exceptions."""

    def __init__(
        self,
        message=None,
        status_code=0,
    ):
        super().__init__(message)
        self.status_code = status_code

    def get_exception(self):
        return self


class BadRequest(DataSolutionsSDKException):
    """Exception for Bad Request."""

    def __init__(self, message="Bad Request"):
        super().__init__(
            message,
            status_code=400,
        )


class UnauthorizedException(DataSolutionsSDKException):
    """Exception for 401 Unauthorized."""

    def __init__(self, message="Unauthorized. Check your API Key."):
        super().__init__(
            message,
            status_code=401,
        )


class ForbiddenException(DataSolutionsSDKException):
    """Exception for 403 Forbidden."""

    def __init__(
        self,
        message="Forbidden. Contact Data Solutions if you believe you should have access to this endpoint/data.",
    ):
        super().__init__(
            message,
            status_code=403,
        )


class ValueException(DataSolutionsSDKException):
    """Exception for the API returning an unexpected response."""

    def __init__(self, message="Invalid selection was made."):
        super().__init__(
            message,
            status_code=400,
        )


class NotFoundException(DataSolutionsSDKException):
    """Exception for 404 Not Found."""

    def __init__(self, message="Not Found. Is your query correct?"):
        super().__init__(
            message,
            status_code=404,
        )


class InternalServerException(DataSolutionsSDKException):
    """Exception for 500 Internal Server Error."""

    def __init__(self, message="Internal Server Error"):
        super().__init__(
            message,
            status_code=500,
        )


class RateLimitExceededException(DataSolutionsSDKException):
    """Exception for 429 Rate Limit Exceeded."""

    def __init__(self, message="Rate Limit Exceeded."):
        super().__init__(
            message,
            status_code=429,
        )


class DataSolutionsAPIException(DataSolutionsSDKException):
    """Exception for the API returning an unexpected response."""

    def __init__(self, message="Unexpected response from the API."):
        super().__init__(
            message,
            status_code=501,
        )


class UnhandledException(DataSolutionsSDKException):
    """Unhandled exception."""

    def __init__(
        self,
        message="An unhandled exception occured. Please contact the Data Solutions Team.",
        details="",
    ):
        super().__init__((message, details))
