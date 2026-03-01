# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from config import MENUS
import random

app = FastAPI(title="AI Enabled Conversational IVR - Hospital")

# -----------------------
# In-Memory Session Store
# -----------------------

sessions = {}

# -----------------------
# Request Models
# -----------------------

class StartCall(BaseModel):
    caller_number: str = "Unknown"

class InputData(BaseModel):
    session_id: str
    digit: str


# -----------------------
# Welcome Prompt
# -----------------------

@app.post("/ivr/start")
def start_call(data: StartCall):

    session_id = f"HOSP_{random.randint(1000,9999)}"

    sessions[session_id] = {
        "current_menu": "main"
    }

    return {
        "session_id": session_id,
        "menu": "main",
        "prompt": MENUS["main"]["prompt"]
    }


# -----------------------
# Menu Handling Logic
# -----------------------

@app.post("/ivr/input")
def handle_input(data: InputData):

    session = sessions.get(data.session_id)

    if not session:
        return {"error": "Session not found"}

    current_menu = session["current_menu"]

    if current_menu not in MENUS:
        return {"error": "Invalid menu"}

    menu = MENUS[current_menu]

    # Check if option exists
    if data.digit not in menu["options"]:
        return {
            "status": "invalid",
            "prompt": menu["prompt"]
        }

    option = menu["options"][data.digit]
    action = option["action"]

    # -----------------------
    # GOTO another menu
    # -----------------------
    if action == "goto":
        target_menu = option["target"]
        session["current_menu"] = target_menu

        return {
            "status": "ok",
            "menu": target_menu,
            "prompt": MENUS[target_menu]["prompt"]
        }

    # -----------------------
    # END call
    # -----------------------
    elif action == "end":
        del sessions[data.session_id]

        return {
            "status": "hangup",
            "message": option["message"]
        }


# -----------------------
# Health Check
# -----------------------

@app.get("/")
def root():
    return {"status": "Hospital IVR Backend Running"}