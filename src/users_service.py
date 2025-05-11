from fastapi import FastAPI, HTTPException
from typing import Dict, List

users_app = FastAPI()

users = [
    {"username": "testuser1", "password": "password123", "email": "testuser1@example.com", "permissions": ["read"]},
    {"username": "testuser2", "password": "securepass", "email": "testuser2@example.com"}, "permissions": ["read", "write"]
]

@users_app.get("/")
async def read_root() -> Dict[str, str]:
    """
    Root endpoint for the users service.

    Returns:
        A dictionary with a message indicating that the users service is running.
    """
    return {"message": "Users Service Running"}

@users_app.get("/users/{username}")
async def read_user(username: str) -> Dict[str, str]:
    """
    Endpoint to retrieve user information by username.

    Args:
        username: The username of the user to retrieve.
    Returns:
        A dictionary containing the user's username and email.
    Raises:
        HTTPException: If the user is not found (status code 404).
    """
    for user in users:
        if user["username"] == username:
            return {"username": user["username"], "email": user["email"]}
    raise HTTPException(status_code=404, detail="User not found")