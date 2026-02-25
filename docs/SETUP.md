# Local Development

## Prerequisites

- Node.js 20+
- Python 3.11+
- Docker Desktop

## Planned Services

- Frontend app on `http://localhost:3000`
- Backend API on `http://localhost:8000`

## Environment Strategy

Each service owns its own `.env.example` file.
Sensitive values must remain out of source control.

## Immediate Next Steps

- Bootstrap Next.js frontend in `frontend/`
- Bootstrap FastAPI backend in `backend/`
- Add Docker Compose stack for local orchestration
