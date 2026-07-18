import pytest
from fastapi.testclient import TestClient
from src.presentation.api.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "environment": "development"}

def test_security_headers_present():
    response = client.get("/health")
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "DENY"
    assert "Strict-Transport-Security" in response.headers

def test_process_event_requires_valid_payload():
    # Sending empty payload should trigger 422 Unprocessable Entity (Pydantic validation)
    response = client.post("/api/v1/process-event", json={})
    assert response.status_code == 422
