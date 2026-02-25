# Visionary Agent Protocol Backend

FastAPI service for real-time Vision AI workflows.

## Architecture

- `app/api/`: REST + WebSocket routes and dependency providers.
- `app/core/`: configuration, middleware, lifecycle, and exception handlers.
- `app/services/`: vision analysis, streaming, realtime connection, and storage services.
- `app/schemas/`: typed request/response contracts.
- `tests/`: API and WebSocket integration coverage.

## Key Endpoints

- `GET /api/v1/health`
- `GET /api/v1/vision/capabilities`
- `POST /api/v1/vision/analyze`
- `POST /api/v1/vision/question`
- `POST /api/v1/vision/upload`
- `WS /api/v1/ws`

## Local Development

Install dependencies with your preferred Python environment manager, then use:

- `make run` to launch backend
- `make test` to run tests
- `make lint` to run static checks

## Environment

Copy values from `.env.example` and provide:

- `OPENAI_API_KEY`
- `OPENAI_MODEL`
