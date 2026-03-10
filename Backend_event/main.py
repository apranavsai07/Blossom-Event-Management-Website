from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import event_routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(event_routes.router)
