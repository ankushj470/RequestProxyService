class RequestParseException(Exception):
    """
    @summary: Exception class to be used while raising exceptions
        related to request object parsing.
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
            related to Timeout
    """
    pass

class RequestMaxedException(Exception):
    """
    @summary: Exception class to be used while raising exceptions
        related to request max outs
    """
    pass
