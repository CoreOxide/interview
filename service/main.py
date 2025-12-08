"""Main application module combining all microservices."""
from fastapi import FastAPI

from service.auth_service import auth_app
from service.auth_utils import create_secured_endpoint
from service.backend_service import backend_app
from service.users_service import users_app

app = FastAPI()

# All the 3 micro services currently reside in a monolith, what can done otherwise and how?
app.include_router(backend_app)
app.include_router(users_app)
app.include_router(auth_app)

# Secure relevant endpoints
SECURED_ENDPOINTS = ["/items/{item_id}"]

for route in app.routes:
    if route.path in SECURED_ENDPOINTS:
        route.endpoint = create_secured_endpoint(route.endpoint)

    #TODO: other endpoints need to be added?

# How we make sure that during server load all relevnt methods being secured?
