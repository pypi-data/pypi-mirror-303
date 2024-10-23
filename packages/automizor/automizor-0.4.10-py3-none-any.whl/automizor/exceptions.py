from requests import Response


class AutomizorError(Exception):
    def __init__(self, message, error=None):
        if error:
            message = f"{message}: {error}"
        super().__init__(message)

    def __str__(self):
        return f"{self.args[0]}"

    @classmethod
    def from_response(cls, response: Response, message: str):
        _STATUS_EXCEPTION_MAP = {
            400: InvalidRequest,
            401: Unauthorized,
            403: Forbidden,
            404: NotFound,
            429: RateLimitExceeded,
            500: InternalServerError,
            502: BadGateway,
            503: ServiceUnavailable,
        }

        try:
            error = dict(response.json()).get("detail", "Unknown error.")
        except Exception:  # pylint: disable=broad-except
            error = response.text

        return _STATUS_EXCEPTION_MAP.get(response.status_code, UnexpectedError)(
            message, error
        )


class BadGateway(AutomizorError):
    pass


class Forbidden(AutomizorError):
    pass


class InternalServerError(AutomizorError):
    pass


class InvalidRequest(AutomizorError):
    pass


class NotFound(AutomizorError):
    pass


class RateLimitExceeded(AutomizorError):
    pass


class ServiceUnavailable(AutomizorError):
    pass


class Unauthorized(AutomizorError):
    pass


class UnexpectedError(AutomizorError):
    pass
