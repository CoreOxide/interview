"""Authentication and authorization utilities."""
from http.client import HTTPException
from typing import Annotated, Any, Dict

from fastapi import Depends, Header

from service.auth_engine import AuthorizationService


async def get_authorizer(authorization: Annotated[str, Header()]) -> Any:
    """
    Extracts the authorization method from the Authorization header.

    Args:
        authorization: The Authorization header value.

    Returns:
        # TODO: what it need to return?

    Raises:
        HTTPException - if the header was not found or invalid.

    """
    if not authorization:
        raise HTTPException(status_code=401, detail="Not authenticated")
    try:
        auth: Any = None
        # TODO: extract authorization information
        return auth
    except Exception as exc:
        raise HTTPException(
            status_code=401, detail="Invalid authentication credentials"
        ) from exc


def create_secured_endpoint(original_endpoint: callable) -> callable:
    """
    Wraps an endpoint to enforce authentication and authorization.

    Args:
        original_endpoint: The original endpoint function to be secured.

    Returns:
        A new endpoint function that includes authentication and authorization checks.
    """

    async def secured_endpoint(payload: Dict[str, Any], auth=Depends(get_authorizer)) -> dict:
        """
        Secured endpoint for accessing internal endpoints.
        """
        credentials = {"auth": auth}  # TODO: Do you think we need something else here?
        authorization_service = AuthorizationService()
        if authorization_service.authorize_request(credentials, original_endpoint):
            # Call the original endpoint logic
            return await original_endpoint(**payload)
        raise HTTPException(status_code=403, detail="Not authorized")

    return secured_endpoint
