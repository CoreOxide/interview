from fastapi import FastAPI

backend_app = FastAPI()

@backend_app.get("/")
async def read_root() -> dict:
    """
    Root endpoint for the backend service.

    Returns:
        A dictionary with a welcome message.
    """
    return {"message": "Backend Service Running from backend_app"}

@backend_app.get("/items/{item_id}")
async def read_item(item_id: int) -> dict:
    """
    Endpoint to retrieve information about a specific item.
    """
    return {"item_id": item_id, "name": f"Item {item_id}", "description": "This is a sample item."}