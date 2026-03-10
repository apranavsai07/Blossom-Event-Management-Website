from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from database import db

router = APIRouter()

# -------------------
# Pydantic Schemas
# -------------------
class User(BaseModel):
    name: str
    email: EmailStr
    password: str

class EventRegistration(BaseModel):
    email: EmailStr
    event_id: str

class Event(BaseModel):  # ✅ This was missing
    id: str
    name: str
    desc: str
    location: str
    date: str    

# -------------------
# User Registration
# -------------------
@router.post("/register_user")
def register_user(user: User):
    if db.users.find_one({"email": user.email}):
        return {"error": "User already exists"}
    db.users.insert_one(user.dict())
    return {"message": "User registered successfully"}

# -------------------
# Register for Event
# -------------------
@router.post("/register_event")
def register_event(reg: EventRegistration):
    if db.registrations.find_one({"email": reg.email, "event_id": reg.event_id}):
        return {"error": "Already registered for this event"}
    db.registrations.insert_one(reg.dict())
    return {"message": "Registered for event"}

# -------------------
# Get Events
# -------------------
@router.get("/events")
def get_events():
    events = list(db.events.find({}, {"_id": 0}))
    return events

@router.post("/create_event")
def create_event(event: Event):
    if db.events.find_one({"id": event.id}):
        return {"error": "Event ID already exists"}
    db.events.insert_one(event.dict())
    return {"message": "Event created successfully"}