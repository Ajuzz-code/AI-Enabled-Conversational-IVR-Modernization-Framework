# tests/test_unit.py

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Hospital IVR" in response.json()["status"]


def test_start_call():
    response = client.post("/ivr/start", json={})
    assert response.status_code == 200
    data = response.json()
    assert "session_id" in data
    assert "prompt" in data


def test_invalid_session():
    response = client.post("/ivr/input", json={
        "session_id": "INVALID",
        "digit": "1"
    })
    assert response.status_code == 200
    assert "error" in response.json()