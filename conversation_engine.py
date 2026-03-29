# conversation_engine.py

from config import PATIENTS

DOCTORS = {
    "general": {
        "Dr Ravi": "10 AM – 12 PM",
        "Dr Meera": "10 AM – 2 PM"
    },
    "cardiology": {
        "Dr Arjun": "11 AM – 1 PM",
        "Dr Sneha": "4 PM – 8 PM"
    },
    "neurology": {
        "Dr Kiran": "12 PM – 4 PM",
        "Dr Anjali": "3 PM – 8 PM"
    },
    "orthopedic": {
        "Dr Raj": "9 AM – 3 PM",
        "Dr Deepa": "5 PM – 10 PM"
    }
}


def process_conversation(session, text):

    text = text.lower()
    state = session.get("conv_state", None)

    # ---------------- START ----------------
    if not state:

        if "appointment" in text:
            session["conv_state"] = "department"
            return "Great! Which department?\nGeneral / Cardiology / Neurology / Orthopedic"

        if "lab" in text or "report" in text:
            session["conv_state"] = "patient_id"
            session["current_menu"] = "lab" 
            return "Please enter your Patient ID"

        return None

    # ---------------- DEPARTMENT ----------------
    if state == "department":

        if "general" in text:
            session["department"] = "general"
        elif "cardio" in text:
            session["department"] = "cardiology"
        elif "neuro" in text:
            session["department"] = "neurology"
        elif "ortho" in text:
            session["department"] = "orthopedic"
        else:
            return "Please choose valid department"

        session["conv_state"] = "doctor"

        doctors = DOCTORS[session["department"]]

        msg = "Available Doctors:\n"
        for name, time in doctors.items():
            msg += f"{name} ({time})\n"

        msg += "\nWhich doctor?"
        return msg

    # ---------------- DOCTOR ----------------
    if state == "doctor":

        dept = session.get("department")
        doctors = DOCTORS.get(dept, {})

        clean_text = text.replace("doctor", "").replace("dr", "").strip()

        for name in doctors:
            doctor_name = name.lower().replace("dr ", "")

            if doctor_name in clean_text or clean_text in doctor_name:

                session["doctor"] = name
                session["time"] = doctors[name]
                session["conv_state"] = "confirm"

                return f"{name} is available at {doctors[name]}\nConfirm booking? (yes/no)"

        return "Please choose a valid doctor"

    # ---------------- CONFIRM ----------------
    if state == "confirm":

        if "yes" in text:
            doctor = session.get("doctor")
            time = session.get("time")

            session["conv_state"] = None

            return f"✅ Appointment booked with {doctor} at {time}"

        if "no" in text:
            session["conv_state"] = "department"
            return "Okay, choose department again"

    # ---------------- PATIENT ID ----------------
    if state == "patient_id":

        if text not in PATIENTS:
            return "Invalid Patient ID. Please try again"

        patient = PATIENTS[text]

        session["patient_id"] = text
        session["conv_state"] = "lab_menu"
        session["current_menu"] = "lab_menu"

        return f"""Patient Name: {patient['name']}

Available Reports:
• Blood Test
• X-Ray
• Scan

Which report do you want?"""

    # ---------------- LAB MENU ----------------
    if state == "lab_menu":

        pid = session.get("patient_id")
        patient = PATIENTS.get(pid)

        if "blood" in text:
            blood = patient["blood"]
            return f"""Blood Report for {patient['name']}:
            Status: {blood['status']}
            Hemoglobin: {blood['hemoglobin']}
            Sugar Level: {blood['sugar']}
            Cholesterol: {blood['cholesterol']}
            """

        if "xray" in text:
            return f"X-Ray Report for {patient['name']}:\nStatus: {patient['xray']}"

        if "scan" in text:
            return f"Scan Report for {patient['name']}:\nStatus: {patient['scan']}"

        return "Please say blood test, xray, or scan report"

    return None