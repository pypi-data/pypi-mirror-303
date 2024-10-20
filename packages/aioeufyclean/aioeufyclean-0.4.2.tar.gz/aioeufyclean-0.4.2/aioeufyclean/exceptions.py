class EufyCleanException(Exception):
    pass


class ConnectionFailed(EufyCleanException):
    pass


class AuthenticationFailed(EufyCleanException):
    pass


class TuyaException(EufyCleanException):
    """Base for Tuya exceptions."""


class InvalidKey(TuyaException):
    """The local key is invalid."""


class InvalidMessage(TuyaException):
    """The message received is invalid."""


class MessageDecodeFailed(TuyaException):
    """The message received cannot be decoded as JSON."""


class ConnectionException(TuyaException):
    """The socket connection failed."""


class ConnectionTimeoutException(ConnectionException):
    """The socket connection timed out."""


class RequestResponseCommandMismatch(TuyaException):
    """The command in the response didn't match the one from the request."""
