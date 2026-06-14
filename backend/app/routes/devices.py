from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Device(BaseModel):
    device_id: str
    name: str
    location: str
    status: str

devices = [
    {
        "device_id": "SG001",
        "name": "Fiber Cabinet 1",
        "location": "Windhoek CBD",
        "status": "online"
    }
]

@router.get("/")
def get_devices():
    return {"devices": devices}

@router.post("/")
def add_device(device: Device):
    devices.append(device.model_dump())
    return {
        "message": "Device added successfully",
        "device": device
    }