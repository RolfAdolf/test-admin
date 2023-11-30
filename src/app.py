from fastapi import FastAPI
from sqladmin import Admin

from db.db_connector import engine
from adminsite import StatusAdmin, CityAdmin, UserAdmin, TaskAdmin, authentication_backend


def create_app():
    app_ = FastAPI()
    
    admin = Admin(
        engine=engine,
        app=app_,
        authentication_backend=authentication_backend,
    )
    
    admin.add_view(StatusAdmin)
    admin.add_view(CityAdmin)
    admin.add_view(UserAdmin)
    admin.add_view(TaskAdmin)
    
    return app_


app = create_app()
