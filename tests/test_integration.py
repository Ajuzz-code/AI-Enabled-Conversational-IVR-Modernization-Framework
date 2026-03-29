# tests/test_integration.py

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_menu_navigation():

    # Step 1: Start session
    start = client.post("/ivr/start", json={})
    session_id = start.json()["session_id"]

    # Step 2: Press 1 (Appointments)
    response = client.post("/ivr/input", json={
        "session_id": session_id,
        "digit": "1"
    })

    assert response.status_code == 200
    assert "appointments" in response.json()["menu"]

    # Step 3: Press 1 again (General Physician)
    response = client.post("/ivr/input", json={
        "session_id": session_id,
        "digit": "1"
    })

    assert response.status_code == 200
    assert response.json()["status"] == "hangup"