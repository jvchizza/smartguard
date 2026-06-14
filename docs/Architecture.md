# SmartGuard Architecture

## Overview

SmartGuard consists of four major components:

1. IoT Device Layer
2. Backend Layer
3. Database Layer
4. Frontend Dashboard

---

## IoT Device Layer

Hardware:

- ESP32
- ESP32-CAM
- Reed Switch
- Buzzer

Responsibilities:

- Detect events
- Capture images
- Send data to backend

---

## Backend Layer

Technology:

- FastAPI

Responsibilities:

- Device registration
- Event processing
- Alert generation
- API services

---

## Database Layer

Technology:

- Supabase PostgreSQL

Responsibilities:

- Store users
- Store devices
- Store events
- Store alerts

---

## Dashboard Layer

Technology:

- Lovable

Responsibilities:

- Device monitoring
- Alert display
- Event history
- Evidence viewing