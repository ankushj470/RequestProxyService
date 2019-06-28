class RequestParseException(Exception):
    """
    @summary: Exception class to be used while raising exceptions
        related to request object parsing.
    """
    pass


class AuthenticationFailureException(Exception):
    """
    @summary: Exception class to be used while raising exceptions
        related to failure of request authentication.
    """
    pass

class ValidationFailureException(Exception):
    """
    @summary: Exception class to be used while raising exceptions
        related to failure in validating the request data.
    """
    pass

class InvalidURLException(Exception):
    """
    @summary: Exception class to be used while raising exceptions
        related to URL issue.
    """
    pass

class TimeOutException(Exception):
    """
    @summary: Exception class to be used while raising exceptions
        related to URL issue.
    """
    pass

class RequestMaxedException(Exception):
    """
    @summary: Exception class to be used while raising exceptions
        related to URL issue.
    """
    pass
