import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from api import app
from config import APP_HOST
# from utilities import logging  # noqa: F401

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(app, host=APP_HOST, port=5000)