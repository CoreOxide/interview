from fastapi import FastAPI
from src.auth_service import AuthenticationService, AuthorizationService


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
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]) -> Optional[Any]:
    """
    Handles user login.

    Args:
        username: The user's username.
        password: The user's password.

    Returns:
        Optionally some response to the user if authentication succeeded.

    Raises:
        HTTPException: If authentication fails due to incorrect credentials.
    """
    auth_service = AuthenticationService()
    authentication_result: Any = auth_service.authenticate_user(username, password)
    if user:
        return {"something": "or nothing"}  # TODO: remove if no return value needed
    else:
        raise HTTPException(status_code=401, detail="Incorrect username or password")


async def get_authorizer(authorization: Annotated[str, Header()]) -> Any:
    """
    Extracts the authorization method from the Authorization header.

    Args:
        authorization: The Authorization header value.

    Returns: The authorization field string if valid.
    """
    if not authorization:
        raise HTTPException(status_code=401, detail="Not authenticated")
    try:
        auth: Any = None
        # TODO: extract authorization information
        return auth
    except ValueError:
        raise HTTPException(
            status_code=401, detail="Invalid authentication credentials"
        )


def create_secured_endpoint(original_endpoint: callable) -> callable:
    """
    Wraps an endpoint to enforce authentication and authorization.

    Args:
        original_endpoint: The original endpoint function to be secured.

    Returns:
        A new endpoint function that includes authentication and authorization checks.
    """
    async def secured_endpoint(item_id: int, auth: Any = Depends(get_authorizer)) -> dict:
        """
        Secured endpoint for accessing item details.
        """
        user = {"username": "", "auth": auth}  # TODO: Do you think we need username here? or authentication information is ehough?
        authorization_service = AuthorizationService()
        if authorization_service.authorize_request(user, "/items/{item_id}"):
            # Call the original endpoint logic
            return await original_endpoint(item_id)
        else:
            raise HTTPException(status_code=403, detail="Not authorized")

    return secured_endpoint