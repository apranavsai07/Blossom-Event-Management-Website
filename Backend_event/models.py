from pydantic import BaseModel

class Event(BaseModel):
    name: str
    date: str
    desc: str
    location: str
    id:str

class Registration(BaseModel):
    user_name: str
    event_id: str
