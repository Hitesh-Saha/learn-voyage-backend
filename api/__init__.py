from fastapi import FastAPI

from . import auth

app = FastAPI(title="Learn Voyage", version="0.1.0")

app.include_router(auth.app)
# app.include_router(event_app.app)
# app.include_router(participants_app.app)
# app.include_router(utilities.app)