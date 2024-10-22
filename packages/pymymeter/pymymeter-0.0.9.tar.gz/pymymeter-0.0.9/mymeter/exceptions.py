"""Exceptions."""


class DataException(Exception):
    """Error to indicate no returned data."""


class TokenErrorException(Exception):
    """Error to indicate no __RequestVerificationToken found."""


class InvalidAuth(Exception):
    """Error to indicate invalid authentication."""
