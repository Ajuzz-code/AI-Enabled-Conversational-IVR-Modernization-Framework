from fastapi.responses import FileResponse
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

from config import MENUS
from middleware import process_menu
from ai_engine import detect_intent
from conversation_engine import process_conversation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

sessions = {}

class StartCall(BaseModel):
    caller_number: str = "Unknown"

class DigitInput(BaseModel):
    session_id: str
    digit: str

class TextInput(BaseModel):
    session_id: str
    text: str

@app.post("/ivr/start")
def start_call(data: StartCall):
    session_id = f"HOSP_{random.randint(1000,9999)}"

    sessions[session_id] = {
        "current_menu": "main",
        "history": [],
        "conv_state": None
    }

    return {
        "session_id": session_id,
        "prompt": "Welcome to Care Hospital\n\n" + MENUS["main"]["prompt"]
    }

@app.post("/ivr/input")
def handle_digit(data: DigitInput):

    session = sessions.get(data.session_id)

    if not session:
        return {"error": "Session not found"}
    
    session["history"].append(data.digit)

    # ✅ RESET conversational state when keypad used
    if session.get("conv_state") == "patient_id":
        pass
    else:

        session["conv_state"] = None

   

    result = process_menu(session, data.digit)

    if result.get("status") == "hangup":
        sessions.pop(data.session_id, None)

    return result

@app.post("/ivr/conversation")
def handle_text(data: TextInput):

    session = sessions.get(data.session_id)

    if not session:
        return {"error": "Session not found"}

    # ✅ TRY CONVERSATION FIRST
    reply = process_conversation(session, data.text)

    if reply:
        return {"prompt": reply}

    # ✅ FALLBACK TO IVR MENU
    digit = detect_intent(data.text, session["current_menu"])

    if digit:
        return process_menu(session, digit)

    return {
        "prompt": "Sorry I didn't understand"
    }

@app.get("/")
def serve_ui():
    return FileResponse("frontend/index.html")