from fastapi import FastAPI
from sqladmin import ModelView
from sqladmin.authentication import AuthenticationBackend
from fastapi.requests import Request

from models import *


class StatusAdmin(ModelView, model=Status):
    name_plural = 'Statuses'
    is_async = True
    column_list = [Status.id, Status.name]


class CityAdmin(ModelView, model=City):
    name_plural = 'Cities'
    is_async = True
    column_list = [City.id, City.name]


class UserAdmin(ModelView, model=User):
    is_async = True
    column_list = [User.id, User.name]


class TaskAdmin(ModelView, model=Task):
    is_async = True
    column_list = [Task.id, Task.name]


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]

        # Validate username/password credentials
        if username != 'admin' and password != 'admin':
            return False

        # And update session
        request.session.update({"token": "..."})

        return True

    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return False

        # Check the token in depth
        return True


authentication_backend = AdminAuth(secret_key="some secret key")
