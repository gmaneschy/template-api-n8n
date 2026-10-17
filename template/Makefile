.PHONY: install dev test lint fmt migrate revision

install:
	uv sync

dev:
	uv run uvicorn app.main:app --reload

test:
	uv run pytest

lint:
	uv run ruff check .
	uv run ruff format --check .

fmt:
	uv run ruff check --fix .
	uv run ruff format .

migrate:
	uv run alembic upgrade head

revision:
	uv run alembic revision --autogenerate -m "$(m)"
