# Architecture Overview

## Monorepo Layout

- `frontend/`: Next.js 14 App Router application (TypeScript + Tailwind + Framer Motion).
- `backend/`: FastAPI service with REST + WebSocket endpoints.
- `docker/`: Local and production container orchestration assets.
- `docs/`: Technical documentation, operational runbooks, and architecture notes.

## System Boundaries

- Frontend: presentation, upload flows, live analysis UI, websocket client.
- Backend API: request routing, validation, auth boundary (future), realtime gateway.
- AI Services: OpenAI vision integration and stream orchestration.
- Infrastructure: containerized runtime and environment-driven config.

## Design Principles

- Clean architecture with clear interfaces between API, domain logic, and integrations.
- Feature-oriented modules with strongly typed contracts.
- Environment-first configuration with secure defaults.
- Real-time first UX with graceful fallback for non-streaming paths.
