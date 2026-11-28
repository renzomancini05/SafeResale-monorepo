"""Test dell'endpoint /health."""

from fastapi.testclient import TestClient

from app.config import get_settings
from app.main import app

client = TestClient(app)


def test_health_risponde_ok():
    """/health risponde 200 con stato "ok"."""
    risposta = client.get("/health")

    assert risposta.status_code == 200
    assert risposta.json()["status"] == "ok"


def test_health_riporta_la_versione_dal_env(monkeypatch):
    """La versione della pipeline arriva dalla configurazione, non dal codice."""
    monkeypatch.setenv("PIPELINE_VERSION", "9.9.9")
    get_settings.cache_clear()
    try:
        risposta = client.get("/health")
        assert risposta.json()["pipelineVersion"] == "9.9.9"
    finally:
        get_settings.cache_clear()
