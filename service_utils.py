class DataFetchException(Exception):
    """
    @summary: Exception class to be used while raising exceptions
        related to data extraction from test database.
    """
    pass

class RequestParseException(Exception):
    """
    @summary: Exception class to be used while raising exceptions
        related to request object parsing.
    """
    pass

class InvalidTestDataException(Exception):
    """
    @summary: Exception class to be used while raising exceptions
        related to either non availability or ambiguous test data.
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

