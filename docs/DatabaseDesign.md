# Database Design

## users

| Field | Type |
|---------|---------|
| id | UUID |
| email | VARCHAR |
| password_hash | VARCHAR |
| created_at | TIMESTAMP |

---

## devices

| Field | Type |
|---------|---------|
| id | UUID |
| user_id | UUID |
| name | VARCHAR |
| type | VARCHAR |
| location | VARCHAR |
| status | VARCHAR |
| created_at | TIMESTAMP |

---

## events

| Field | Type |
|---------|---------|
| id | UUID |
| device_id | UUID |
| event_type | VARCHAR |
| severity | VARCHAR |
| image_url | TEXT |
| created_at | TIMESTAMP |

---

## alerts

| Field | Type |
|---------|---------|
| id | UUID |
| event_id | UUID |
| status | VARCHAR |
| sent_at | TIMESTAMP |