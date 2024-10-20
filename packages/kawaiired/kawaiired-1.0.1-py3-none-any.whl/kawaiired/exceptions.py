class KawaiiException(Exception):
    """Base class for all Kawaii exceptions."""


class APIException(KawaiiException):
    """Exception due to an error response from the kawaii.red API."""

    def __init__(self, status: int, reason: str, message: str):
        """
        Initialize the APIException.

        Args:
            status (int): The status code of the response.
            reason (str): The reason why the response failed.
            message (str): The message to be displayed.
        """
        super().__init__(f"{status} {reason}: {message}")


class InvalidCategory(KawaiiException):
    """Exception due to an invalid category."""

    def __init__(self, category: str):
        """
        Initialize the InvalidCategory exception.

        Args:
            category (str): The category that is invalid.
        """
        super().__init__(f"Invalid category: {category}")


class InvalidToken(KawaiiException):
    """Exception due to an invalid token."""

    def __init__(self, token: str):
        """
        Initialize the InvalidToken exception.

        Args:
            token (str): The token that is invalid.
        """
        super().__init__(f"Invalid token: {token}")


class TokenMissing(KawaiiException):
    """Exception due to a missing token."""

    def __init__(self):
        """Initialize the TokenMissing exception."""
        super().__init__("Missing token")
