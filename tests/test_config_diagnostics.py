"""Tests for centralized configuration and system diagnostics."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "backend"
sys.path.insert(0, str(ROOT))

from app import app
from config import config
from diagnostics import get_system_diagnostics

def test_config_defaults():
    assert config.DEFAULT_MODEL == "Nexa Reasoner"
    assert config.API_PREFIX == "/api"
    assert config.PORT == 8000
    assert config.MAX_TOKENS_PER_REQUEST > 0

def test_system_diagnostics():
    diag = get_system_diagnostics()
    assert diag["status"] == "healthy"
    assert "environment" in diag
    assert diag["environment"]["active_domain_modules"] > 0
    assert "version" in diag

def test_extended_health_endpoint():
    client = app.test_client()
    res = client.get("/api/health/extended")
    assert res.status_code == 200
    data = res.get_json()
    assert data["status"] == "healthy"
    assert "store_counts" in data
