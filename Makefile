.PHONY: install test run backend frontend docker-up

install:
	cd backend && python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

test:
	cd backend && . .venv/bin/activate 2>/dev/null; PYTHONPATH=backend pytest tests/ -q --cov=backend --cov-report=term-missing || PYTHONPATH=backend python -m pytest tests/ -q

run: backend

backend:
	cd backend && python app.py

frontend:
	cd frontend && python -m http.server 5173

docker-up:
	cd docker && docker compose up --build

help:
	@echo "NexaAI: make install|test|backend|frontend|docker-up"
