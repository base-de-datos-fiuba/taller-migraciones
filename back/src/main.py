# main.py
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict
from src.service.users import UserService

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class User(BaseModel):
    name: str
    email: str

@app.post("/users/")
def create_user(user: User) -> Dict[str, str]:
    """
    Creates a new user with the provided name and email.
    """
    result = UserService.create_user(user.name, user.email)
    return {
        "name": result.name,
        "email": result.email
    }
