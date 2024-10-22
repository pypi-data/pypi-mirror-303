"""Midea Lan library exceptions."""

from __future__ import annotations


class MideaLanError(Exception):
    """Base class for mideal_local errors."""


class CannotAuthenticate(MideaLanError):
    """Exception raised when credentials are incorrect."""


class CannotConnect(MideaLanError):
    """Exception raised when connection fails."""


class DataUnexpectedLength(MideaLanError):
    """Exception raised when data length is less or more than expected."""


class DataSignDoesntMatch(MideaLanError):
    """Exception raised when data sign is not matching."""


class DataSignWrongType(MideaLanError):
    """Exception raised when data is the wrong type to sign."""


class ElementMissing(MideaLanError):
    """Exception raised when a element is missing."""


class MessageWrongFormat(MideaLanError):
    """Exception raised when message format is wrong."""


class SocketException(MideaLanError):
    """Exception raise by socket error."""


class ValueWrongType(MideaLanError):
    """Exception raised when the value has a wrong data type."""
