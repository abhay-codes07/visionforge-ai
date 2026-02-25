.PHONY: up down logs dev-frontend dev-backend test-backend

up:
	docker compose -f docker/docker-compose.yml up -d --build

down:
	docker compose -f docker/docker-compose.yml down

logs:
	docker compose -f docker/docker-compose.yml logs -f

dev-frontend:
	npm run dev:frontend

dev-backend:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 --app-dir backend

test-backend:
	pytest backend/tests
