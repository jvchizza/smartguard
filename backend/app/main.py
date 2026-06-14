from fastapi import FastAPI
from backend.app.routes.devices import router as device_router
from backend.app.routes.events import router as event_router
from backend.app.routes.alerts import router as alert_router

app = FastAPI(
    title="SmartGuard API",
    version="1.0.0"
)

app.include_router(
    device_router,
    prefix="/devices",
    tags=["Devices"]
)
app.include_router(
    event_router,
    prefix="/events",
    tags=["Events"]
)
app.include_router(
    alert_router,
    prefix="/alerts",
    tags=["Alerts"]
)
@app.get("/")
def root():
    return {
        "message": "SmartGuard API Running"
    }