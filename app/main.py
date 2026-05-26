from fastapi import FastAPI

from app.routes.auth_routes import router as auth_router
from app.routes.task_routes import router as task_router

from app.middleware.logging_middleware import log_requests

# NEW IMPORTS
from app.database import engine, Base

from app.models.task_model import Task
from app.models.user_model import User


# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.middleware("http")(log_requests)

app.include_router(auth_router)
app.include_router(task_router)

@app.get("/")
def home():

    return {
        "message": "Welcome to TaskFlow API"
    }