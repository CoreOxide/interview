import requests
from typing import Any, Dict

def interact_with_backend() -> None:
    """
    Interacts with the combined backend service's root endpoint and prints the response.
    """
    try:
        response = requests.get("http://localhost:8000/")
        response.raise_for_status()
        print("Combined Service Root Response:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error interacting with Combined Service Root: {e}")
    
def get_item_info(item_id: int) -> None:
    """
    Retrieves information for a specific item from the backend service.

    Args:
        item_id: The ID of the item to retrieve.
    """
    try:
        response = requests.get(f"http://localhost:8000/items/{item_id}")
        response.raise_for_status()
        print(f"Item Info (Item ID: {item_id}):", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error getting item info: {e}")


def get_user_info(username: str) -> None:
    """
    Retrieves information for a specific user from the users service.

    Args:
        username: The username of the user to retrieve.
    """
    try:
        response = requests.get(f"http://localhost:8000/users/{username}")
        response.raise_for_status()
        print(f"User Info (Username: {username}):", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error getting user info: {e}")


if __name__ == "__main__":
    interact_with_backend()
    # TODO: do we need to store some data locally?
    get_item_info(1)
    get_user_info("testuser1")