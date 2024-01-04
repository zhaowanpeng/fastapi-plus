from fastapi import FastAPI
from user import user_router

app = FastAPI()

app.include_router(user_router, prefix="/api")
