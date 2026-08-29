# NexaAI Platform

A production-oriented AI SaaS platform starter with chat, documents, agents, analytics, auth, billing, API keys, and an admin dashboard.

## Install

```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
pip install -r requirements.txt
# or: pip install -r requirements.lock
```

## Build

```bash
# Optional: build container image
docker build -t nexa-ai .
# or via compose
cd docker && docker compose build
```

## Run

### Backend
```bash
cd backend
python app.py
# or: make backend
```
API: http://localhost:8000  
Health: http://localhost:8000/api/health

### Frontend
```bash
cd frontend
python -m http.server 5173
# or: make frontend
```
UI: http://localhost:5173

### Tests
```bash
pip install -r backend/requirements.txt
PYTHONPATH=backend pytest tests/ -q --cov=backend
# or: make test
```

### Docker
```bash
docker build -t nexa-ai .
docker run -p 8000:8000 nexa-ai
# or: make docker-up
```

See docs/ for module notes.
