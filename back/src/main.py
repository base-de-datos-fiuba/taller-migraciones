# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.control.users import router as users_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
