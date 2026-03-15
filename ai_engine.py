# ai_engine.py

def detect_intent(text):

    text = text.lower()

    if "appointment" in text or "doctor" in text or "book" in text:
        return "1"

    if "lab" in text or "report" in text:
        return "2"

    if "bill" in text or "payment" in text:
        return "3"

    if "reception" in text or "help" in text:
        return "9"

    return None