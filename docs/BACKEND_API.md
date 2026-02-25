# Backend API Contract

## Base URL

- Local: `http://localhost:8000/api/v1`

## REST Endpoints

### Health

- `GET /health`
- Response:

```json
{
  "status": "ok",
  "service": "visionary-agent-protocol-backend"
}
```

### Vision Capabilities

- `GET /vision/capabilities`
- Response includes:
  - `supported_media_types`
  - `supported_transports`
  - `supports_streaming`
  - `model`

### Vision Analyze

- `POST /vision/analyze`
- Request:

```json
{
  "media_type": "image",
  "prompt": "Describe the scene"
}
```

### Vision Question

- `POST /vision/question`
- Request:

```json
{
  "request_id": "req-123",
  "question": "What objects are visible?"
}
```

### Vision Upload

- `POST /vision/upload`
- Multipart form fields:
  - `media_type`: `image | video | webcam`
  - `file`: binary payload

## WebSocket

### Endpoint

- `ws://localhost:8000/api/v1/ws`

### Inbound Events

- `ping`
- `analyze`
- `question`

### Outbound Events

- `connected`
- `analysis`
- `token`
- `completed`
- `error`

## Local Commands

- Run API:
  - `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`
- Run tests:
  - `pytest`
