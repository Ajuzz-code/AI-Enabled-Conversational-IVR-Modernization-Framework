from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from config import MENUS
from middleware import process_menu
from ai_engine import detect_intent
import random

app = FastAPI(title="Hospital Conversational IVR")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

sessions = {}
call_logs = []

# -------------------
# Request Models
# -------------------

class StartCall(BaseModel):
    caller_number: str = "Unknown"


class DigitInput(BaseModel):
    session_id: str
    digit: str


class TextInput(BaseModel):
    session_id: str
    text: str


# -------------------
# Start Call
# -------------------

@app.post("/ivr/start")
def start_call(data: StartCall):

    session_id = f"HOSP_{random.randint(1000,9999)}"

    sessions[session_id] = {
        "current_menu": "main"
    }

    call_logs.append({
        "session_id": session_id,
        "event": "call_started"
    })

    return {
        "session_id": session_id,
        "prompt": MENUS["main"]["prompt"]
    }


# -------------------
# Keypad Input
# -------------------

@app.post("/ivr/input")
def handle_digit(data: DigitInput):

    session = sessions.get(data.session_id)

    if not session:
        return {"error": "Session not found"}

    call_logs.append({
        "session_id": data.session_id,
        "digit": data.digit
    })

    result = process_menu(session, data.digit)

    if result.get("status") == "hangup":
        sessions.pop(data.session_id, None)

    return result


# -------------------
# Conversational Input
# -------------------

@app.post("/ivr/conversation")
def handle_text(data: TextInput):

    session = sessions.get(data.session_id)

    if not session:
        return {"error": "Session not found"}

    call_logs.append({
        "session_id": data.session_id,
        "text": data.text
    })

    digit = detect_intent(data.text)

    if not digit:
        return {
            "prompt": "Sorry I didn't understand. Please say appointment, lab report, or billing."
        }

    result = process_menu(session, digit)

    if result.get("status") == "hangup":
        sessions.pop(data.session_id, None)

    return result


# -------------------
# Analytics
# -------------------

@app.get("/analytics")
def analytics():

    return {
        "total_logs": len(call_logs),
        "logs": call_logs
    }


# -------------------
# Health Check
# -------------------

@app.get("/")
def root():
    return {"status": "Hospital IVR Running"}