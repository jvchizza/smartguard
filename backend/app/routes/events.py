from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Event(BaseModel):
    device_id: str
    event_type: str

events = []

@router.get("/")
def get_events():
    return {
        "events": events
    }

@router.post("/")
def create_event(event: Event):
    events.append(event.model_dump())

    return {
        "message": "Event recorded",
        "event": event
    }