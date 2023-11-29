from fastapi import FastAPI
from sqladmin import Admin

from db.db_connector import engine
from adminsite import StatusAdmin, CityAdmin, UserAdmin, TaskAdmin, authentication_backend


app = FastAPI()

admin = Admin(
    engine=engine,
    app=app,
    authentication_backend=authentication_backend,
)


admin.add_view(StatusAdmin)
admin.add_view(CityAdmin)
admin.add_view(UserAdmin)
admin.add_view(TaskAdmin)
