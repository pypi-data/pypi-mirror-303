"""Module providing exceptions for each JSON-RPC 2.0 error.

There is one Exception defined for each pre-defined JSON-RPC 2.0 error.
Additionally, there is a ServerError for implementation-defined errors.

Each exception extends a base exception JSONRPCError.
"""

from __future__ import annotations

import warnings

__all__ = (
    "INTERNAL_ERROR",
    "INVALID_PARAMS",
    "INVALID_REQUEST",
    "InternalError",
    "InvalidParams",
    "InvalidRequest",
    "JSONRPCError",
    "METHOD_NOT_FOUND",
    "MethodNotFound",
    "PARSE_ERROR",
    "ParseError",
    "ServerError",
)

from typing import Any, Optional

from jsonrpcobjects.objects import DataError, Error, ErrorType

INTERNAL_ERROR = Error(code=-32603, message="Internal error")
INVALID_PARAMS = Error(code=-32602, message="Invalid params")
INVALID_REQUEST = Error(code=-32600, message="Invalid Request")
METHOD_NOT_FOUND = Error(code=-32601, message="Method not found")
PARSE_ERROR = Error(code=-32700, message="Parse error")


class JSONRPCError(Exception):
    """Base error that all JSON RPC exceptions extend."""

    def __init__(self, error: ErrorType) -> None:
        """Init base JSON-RPC 2.0 error."""
        msg = f"{error.code}: {error.message}"
        self.rpc_error = error
        if isinstance(error, DataError):
            msg += f"\nError Data: {error.data}"
        super(JSONRPCError, self).__init__(msg)


class ParseError(JSONRPCError):
    """Error raised when invalid JSON was received by the server."""

    def __init__(self, data: Optional[Any] = None) -> None:
        """Init JSON-RPC 2.0 invalid JSON error."""
        if data is not None:
            error = DataError(
                code=PARSE_ERROR.code, message=PARSE_ERROR.message, data=data
            )
        else:
            error = PARSE_ERROR
        super(ParseError, self).__init__(error)


class InvalidRequestError(JSONRPCError):
    """Error raised when the JSON sent is not a valid Request object."""

    def __init__(self, data: Optional[Any] = None) -> None:
        """Init JSON-RPC 2.0 invalid request error."""
        if data is not None:
            error = DataError(
                code=INVALID_REQUEST.code, message=INVALID_REQUEST.message, data=data
            )
        else:
            error = INVALID_REQUEST
        super(InvalidRequestError, self).__init__(error)


class MethodNotFoundError(JSONRPCError):
    """Error raised when the method does not exist / is not available."""

    def __init__(self, data: Optional[Any] = None) -> None:
        """Init JSON-RPC 2.0 method not found error."""
        if data is not None:
            error = DataError(
                code=METHOD_NOT_FOUND.code, message=METHOD_NOT_FOUND.message, data=data
            )
        else:
            error = METHOD_NOT_FOUND
        super(MethodNotFoundError, self).__init__(error)


class InvalidParamsError(JSONRPCError):
    """Error raised when invalid method parameter(s) are supplied."""

    def __init__(self, data: Optional[Any] = None) -> None:
        """Init JSON-RPC 2.0 invalid params error."""
        if data is not None:
            error = DataError(
                code=INVALID_PARAMS.code, message=INVALID_PARAMS.message, data=data
            )
        else:
            error = INVALID_PARAMS
        super(InvalidParamsError, self).__init__(error)


class InvalidRequest(JSONRPCError):  # noqa: N818
    """Error raised when the JSON sent is not a valid Request object."""

    def __init__(self, data: Optional[Any] = None) -> None:
        """Init JSON-RPC 2.0 invalid request error."""
        if data is not None:
            error = DataError(
                code=INVALID_REQUEST.code, message=INVALID_REQUEST.message, data=data
            )
        else:
            error = INVALID_REQUEST
        msg = "InvalidRequest is deprecated, use InvalidRequestError"
        warnings.warn(msg, stacklevel=2)
        super(InvalidRequest, self).__init__(error)


class MethodNotFound(JSONRPCError):  # noqa: N818
    """Error raised when the method does not exist / is not available."""

    def __init__(self, data: Optional[Any] = None) -> None:
        """Init JSON-RPC 2.0 method not found error."""
        if data is not None:
            error = DataError(
                code=METHOD_NOT_FOUND.code, message=METHOD_NOT_FOUND.message, data=data
            )
        else:
            error = METHOD_NOT_FOUND
        msg = "MethodNotFound is deprecated, use MethodNotFoundError"
        warnings.warn(msg, stacklevel=2)
        super(MethodNotFound, self).__init__(error)


class InvalidParams(JSONRPCError):  # noqa: N818
    """Error raised when invalid method parameter(s) are supplied."""

    def __init__(self, data: Optional[Any] = None) -> None:
        """Init JSON-RPC 2.0 invalid params error."""
        if data is not None:
            error = DataError(
                code=INVALID_PARAMS.code, message=INVALID_PARAMS.message, data=data
            )
        else:
            error = INVALID_PARAMS
        msg = "InvalidParams is deprecated, use InvalidParamsError"
        warnings.warn(msg, stacklevel=2)
        super(InvalidParams, self).__init__(error)


class InternalError(JSONRPCError):
    """Error raised when there is an internal JSON-RPC error."""

    def __init__(self, data: Optional[Any] = None) -> None:
        """Init a JSON-RPC 2.0 internal error."""
        if data is not None:
            error = DataError(
                code=INTERNAL_ERROR.code, message=INTERNAL_ERROR.message, data=data
            )
        else:
            error = INTERNAL_ERROR
        super(InternalError, self).__init__(error)


class ServerError(JSONRPCError):
    """Error raised when a server error occurs."""

    def __init__(self, code: int, message: str, data: Optional[Any] = None) -> None:
        """Init JSON-RPC 2.0 server error.

        :param code: JSON-RPC 2.0 error code.
        :param message: Error message.
        :param data: Optional error data.
        """
        if data is not None:
            error = DataError(code=code, message=message, data=data)
        else:
            error = Error(code=code, message=message)
        super(ServerError, self).__init__(error)
