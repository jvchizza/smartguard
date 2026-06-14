from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Alert(BaseModel):
    device_id: str
    alert_type: str
    severity: str

alerts = []

@router.get("/")
def get_alerts():
    return {
        "alerts": alerts
    }

@router.post("/")
def create_alert(alert: Alert):
    alerts.append(alert.model_dump())

    return {
        "message": "Alert created",
        "alert": alert
    }