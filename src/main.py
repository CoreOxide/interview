from fastapi import FastAPI, HTTPException, Depends, Form, Header
from typing import Annotated
from src.auth_service import AuthenticationService, AuthorizationService

from src.backend_service import backend_app as backend_routes
from src.users_service import users_app as users_routes


app = FastAPI()


async def get_token(authorization: Annotated[str, Header()]) -> str:
    """
    Extracts the token from the Authorization header.

    Args:
        authorization: The Authorization header value.

    Returns: The token string if valid.
    """
    if not authorization:
        raise HTTPException(status_code=401, detail="Not authenticated")
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(
                status_code=401, detail="Invalid authentication credentials"
            )
        return token
    except ValueError:
        raise HTTPException(
            status_code=401, detail="Invalid authentication credentials"
        )
    
@app.post("/auth/token")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]) -> dict:
    """
    Handles user login and returns an access token.

    Args:
        username: The user's username.
        password: The user's password.

    Returns:
        A dictionary containing the access token, token type, and user information if authentication is successful.

    Raises:
        HTTPException: If authentication fails due to incorrect credentials.
    """
    auth_service = AuthenticationService()
    user = auth_service.authenticate_user(username, password)
    if user:
        return {"access_token": "dummy_token", "token_type": "bearer", "user": user}
    else:
        raise HTTPException(status_code=401, detail="Incorrect username or password")


def create_secured_endpoint(original_endpoint: callable) -> callable:
    """
    Wraps an endpoint to enforce authentication and authorization.

    Args:
        original_endpoint: The original endpoint function to be secured.

    Returns:
        A new endpoint function that includes authentication and authorization checks.
    """
    async def secured_endpoint(item_id: int, token: str = Depends(get_token)) -> dict:
        """
        Secured endpoint for accessing item details.
        """
        user = {"username": "testuser"}  # Replace with actual user retrieval from token
        authorization_service = AuthorizationService()
        if authorization_service.authorize_request(user, "/items/{item_id}"):
            # Call the original endpoint logic
            return await original_endpoint(item_id)
        else:
            raise HTTPException(status_code=403, detail="Not authorized")

    return secured_endpoint


# Include backend routes
app.include_router(backend_routes)

# Secure the /items/{item_id} endpoint
secured = False
for route in app.routes:
    if route.path == "/items/{item_id}" and "GET" in route.methods:
        route.endpoint = create_secured_endpoint(route.endpoint)
        secured = True
        break  # Stop searching once the route is found and modified

if not secured:
    raise Exception("Failed to secure /items/{item_id}")

# Include users routes
app.include_router(users_routes)