from fastapi import FastAPI
from app.api import auth_routes

app = FastAPI(title="Secure File System", description="Secure File System API", version="1.0.0")

app.include_router(auth_routes.router, prefix="/auth")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Secure File System API"}

