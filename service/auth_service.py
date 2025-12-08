"""Authentication service module."""
from typing import Annotated, Any, Optional

from fastapi import FastAPI, Form

from service.auth_engine import AuthenticationService
from service.backend_service import backend_app

auth_app = FastAPI()

@auth_app.get("/")
async def read_root() -> dict:
    """
    Root endpoint for the auth service.

    Returns:
        A dictionary with a welcome message.
    """
    return {"message": "Authentication Service Running from auth_app"}

@backend_app.post("/login")
async def login(
    username: Annotated[str, Form()], password: Annotated[str, Form()]
) -> Optional[Any]:
    """
    Handles user login.

    Args:
        username: The user's username.
        password: The user's password.

    Returns:
        Optionally some response if authentication succeeded.

    Raises:
        HTTPException: If authentication fails due to incorrect credentials.
    """
    try:
        auth_service = AuthenticationService()
        authentication_result: Any = auth_service.authenticate_user(username, password)
        return authentication_result
    except (ValueError, KeyError, NotImplementedError):
        return {
            "status_code": 401,
            "message": "Incorrect username or password"
        }
