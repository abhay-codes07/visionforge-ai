# AI Integration Guide

This document describes how Visionary Agent Protocol integrates OpenAI Vision for REST, SSE, and WebSocket workflows.

## Enable OpenAI Integration

In `backend/.env`:

```env
OPENAI_ENABLED=true
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-4.1-mini
OPENAI_TIMEOUT_SECONDS=30
OPENAI_MAX_RETRIES=2
OPENAI_RETRY_BACKOFF_SECONDS=0.75
OPENAI_FALLBACK_TO_STUB=true
```

If `OPENAI_ENABLED=false`, the backend uses deterministic stub responses.

## REST Flows

### Analyze (JSON)

- `POST /api/v1/vision/analyze`
- Body:

```json
{
  "media_type": "image",
  "prompt": "Describe this scene",
  "source_uri": "https://example.com/frame.jpg"
}
```

### Question (JSON)

- `POST /api/v1/vision/question`
- Body:

```json
{
  "request_id": "req-123",
  "question": "What objects are visible?"
}
```

## SSE Flows

### Analyze Stream

- `POST /api/v1/vision/analyze/stream`
- Emits `data: {"request_id":"...","token":"...","index":0}` chunks
- Terminates with `data: [DONE]`

### Question Stream

- `POST /api/v1/vision/question/stream`
- Emits token chunks and then `data: [DONE]`

## WebSocket Flow

- `WS /api/v1/ws`
- Inbound messages:
  - `{ "type": "ping", "request_id": "..." }`
  - `{ "type": "analyze", "media_type": "image", "prompt": "..." }`
  - `{ "type": "question", "request_id": "...", "question": "..." }`
- Outbound event types:
  - `connected`
  - `analysis`
  - `token`
  - `completed`
  - `error`

## Frontend Integration Points

- `frontend/lib/ai-client.ts`
  - `analyzeVision(...)`
  - `streamAnalyzeVision(...)`
  - `streamQuestionVision(...)`
  - `createVisionWebSocket()`
- `frontend/components/home/agent-studio.tsx`
  - Upload + analyze + SSE token rendering
- `frontend/components/home/live-agent-feed.tsx`
  - Realtime WebSocket console

## Demo Runbook

1. Start backend: `make run` (from `backend/`)
2. Start frontend: `npm run dev:frontend` (from repo root)
3. Open homepage and use:
   - Vision Agent Studio for upload + SSE
   - Live Agent Feed for WebSocket events
