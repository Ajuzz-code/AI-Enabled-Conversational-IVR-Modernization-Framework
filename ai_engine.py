# ai_engine.py

def detect_intent(text, current_menu="main"):

    text = text.lower()

    # MAIN MENU
    if current_menu == "main":

        if any(word in text for word in ["appointment", "doctor", "book"]):
            return "1"

        if any(word in text for word in ["lab", "report", "test"]):
            return "2"

        if any(word in text for word in ["bill", "payment", "amount"]):
            return "3"

        if any(word in text for word in ["help", "reception"]):
            return "9"

    # APPOINTMENTS MENU
    if current_menu == "appointments":

        if "general" in text or "physician" in text:
            return "1"

        if "cardio" in text or "heart" in text:
            return "2"

        if "neuro" in text or "brain" in text:
            return "3"

        if "ortho" in text or "bone" in text:
            return "4"
    
    if current_menu in ["lab_menu", "blood_report", "xray_report", "scan_report"]:

        if "blood" in text:
            return "1"

        if "xray" in text or "x-ray" in text:
            return "2"

        if "scan" in text:
            return "3"

    return None