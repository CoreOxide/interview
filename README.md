# Backend Server Security Task

This is a minimal implementation of a backed service, broken into serveral micro-services. All Apis are publickle accessible. Your task is to secure this service.

## Getting Started

#### Go over the project files
1. All `_service.py` files expose APIs and helper functions for the service. You have `TODO:` comments in areas you need to pay attention to.
2. `main.py` file launches the werserver with all of it's micro-services, and adds all API endpoints to Flask. You don't have to be familliar with Flask.
3. The `auth_engine.py` file is just an interface. You need to implement the logic there.
4. There is also an `api_client.py` which consumes some of the endpoints that this webserver exposes. You should also see if it needs to be adjusted slightly as you add security layers to the webserver.

#### Discuss strategy
How did you choose to secure the webserver? Is this the best method for the task? What did you weigh it against?

Discuss your course of action. What will you implement first? why?

What is the difference between Authorization and Authentication?

What does the webserver need to "remember"? does the client need to save some additional information?
