"""Health and core API smoke tests for NexaAI."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from app import app


def test_health_endpoint():
    client = app.test_client()
    res = client.get("/api/health")
    assert res.status_code == 200
    data = res.get_json()
    assert data["status"] == "ok"
    assert "service" in data


def test_dashboard_endpoint():
    client = app.test_client()
    res = client.get("/api/dashboard")
    assert res.status_code == 200
    data = res.get_json()
    assert "usage" in data
    assert "users" in data


def test_create_chat():
    client = app.test_client()
    res = client.post("/api/chats", json={"title": "Test Chat"})
    assert res.status_code == 201
    data = res.get_json()
    assert data["title"] == "Test Chat"
    assert "id" in data


def test_create_document():
    client = app.test_client()
    res = client.post("/api/documents", json={"name": "Spec.pdf"})
    assert res.status_code == 201
    assert res.get_json()["status"] == "indexed"


def test_create_agent():
    client = app.test_client()
    res = client.post("/api/agents", json={"name": "Researcher", "model": "Nexa Reasoner"})
    assert res.status_code == 201
    assert res.get_json()["status"] == "active"


def test_echo():
    client = app.test_client()
    res = client.post("/api/echo", json={"message": "hello"})
    assert res.status_code == 200
    assert "reply" in res.get_json()
