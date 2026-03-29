# tests/test_e2e.py

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_full_ivr_flow():

    # Step 1: Start IVR
    start = client.post("/ivr/start", json={})
    data = start.json()

    session_id = data["session_id"]
    assert start.status_code == 200

    # Step 2: Go to Lab Reports
    step1 = client.post("/ivr/input", json={
        "session_id": session_id,
        "digit": "2"
    })

    assert step1.status_code == 200
    assert "lab" in step1.json()["menu"]

    # Step 3: Check lab status
    step2 = client.post("/ivr/input", json={
        "session_id": session_id,
        "digit": "1"
    })

    assert step2.status_code == 200
    assert step2.json()["status"] == "hangup"

    print("✅ Full IVR flow completed successfully")