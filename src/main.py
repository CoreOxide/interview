from fastapi import FastAPI, HTTPException, Depends, Form, Header
from typing import Annotated
from src.auth_service import create_secured_endpoint

from src.backend_service import backend_app as backend_routes
from src.users_service import users_app as users_routes
from src.auth_service import auth_app as auth_routes


app = FastAPI()


app.include_router(backend_routes)
app.include_router(users_routes)
app.include_router(auth_routes)

# Secure the /items/{item_id} endpoint
secured = False
for route in app.routes:
    # TODO: any additional endpoint we want to secure?
    if route.path == "/items/{item_id}" and "GET" in route.methods:
        route.endpoint = create_secured_endpoint(route.endpoint)
        secured = True
        break  # Stop searching once the route is found and modified

if not secured:
    raise Exception("Failed to secure /items/{item_id}")
