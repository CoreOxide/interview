"""Authentication and authorization engine."""
from typing import Any

_USER_CREDS = [
    {"username": "testuser2", "password": "securepass"}
]

_USER_PERMISSION = {
    "testuser2": {
        "permissions": ["/items/*"]
    }
}


class AuthenticationService:
    """
    Provides authentication services.
    """

    def authenticate_user(self, username: str, password: str) -> Any:
        """
        Authenticates a user based on the provided username and password.

        Args:
            username: The username of the user.
            password: The user's password.

        Returns:
            # TODO: what it need to return?

        Raises:
            # TODO: what it need to raise?
        """
        raise NotImplementedError


class AuthorizationService:
    """
    Provides authorization services.
    """

    def authorize_request(self, credentials: dict, endpoint: str) -> Any:
        """
        Authorizes a user's request to access a specific endpoint.

        Args:
            credentials: A dictionary containing user information.
            endpoint: The endpoint being accessed.

        Returns:
            # TODO: what it need to return?

        Raises:
            # TODO: what it need to raise?
        """
        raise NotImplementedError
