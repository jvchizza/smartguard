# SmartGuard Use Cases

## 1. Telecom Cabinet Theft Detection

### Scenario

An unauthorized person opens a telecom, fiber, or copper cable enclosure.

### Process

1. Reed switch detects cabinet door opening.
2. ESP32 sends event to SmartGuard API.
3. SmartGuard records the event.
4. Risk assessment is performed.
5. Alert is generated.
6. Camera captures image evidence.
7. Security personnel are notified.

### Events

door_opened
motion_detected
camera_capture
alert_generated

### Risk Level

HIGH

---

## 2. Vehicle Battery Theft Detection

### Scenario

An individual attempts to remove a vehicle battery.

### Process

1. Battery compartment is opened.
2. Sensor detects unauthorized access.
3. ESP32 sends event to SmartGuard API.
4. Event is recorded.
5. Alert is generated.
6. Camera captures image evidence.

### Events

battery_cover_opened
camera_capture
alert_generated

### Risk Level

HIGH

---

## 3. Vehicle Mirror Theft Detection

### Scenario

An individual attempts to remove or tamper with a vehicle side mirror.

### Process

1. Sensor detects mirror movement.
2. ESP32 sends event to SmartGuard API.
3. Event is recorded.
4. Alert is generated.
5. Camera captures image evidence.

### Events

mirror_movement_detected
camera_capture
alert_generated

### Risk Level

MEDIUM

---

## 4. Tyre Theft Detection

### Scenario

An individual attempts to remove a vehicle wheel or tyre.

### Process

1. Wheel movement or lift detection occurs.
2. ESP32 sends event to SmartGuard API.
3. Event is recorded.
4. Alert is generated.
5. Camera captures image evidence.

### Events

wheel_movement_detected
camera_capture
alert_generated

### Risk Level

HIGH

---

## 5. Retail Theft Detection

### Scenario

A secured retail cabinet, shelf, or stock area is accessed without authorization.

### Process

1. Cabinet or storage area is opened.
2. Motion is detected.
3. SmartGuard records the event.
4. Alert is generated.
5. Camera captures image evidence.

### Events

cabinet_opened
motion_detected
camera_capture
alert_generated

### Risk Level

HIGH

---

# SmartGuard Prototype Scope (Version 1)

The first working SmartGuard prototype will focus on:

1. Telecom cabinet protection
2. Reed switch intrusion detection
3. ESP32 event transmission
4. Camera image capture
5. FastAPI backend processing
6. Alert generation
7. Event logging

Future versions will expand into:

- Vehicle battery protection
- Vehicle mirror protection
- Tyre protection
- Retail asset protection
- AI image analysis
- Predictive theft detection