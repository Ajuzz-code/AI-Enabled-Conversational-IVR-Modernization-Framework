# config.py

MENUS = {
    "main": {
        "prompt": "Welcome to Care Hospital. Press 1 for Appointments, 2 for Lab Reports, 3 for Billing, 9 for Reception.",
        "options": {
            "1": {"action": "goto", "target": "appointments"},
            "2": {"action": "goto", "target": "lab"},
            "3": {"action": "goto", "target": "billing"},
            "9": {"action": "end", "message": "Connecting you to Reception. Thank you."}
        }
    },

    "appointments": {
        "prompt": "Press 1 for General Physician, 2 for Cardiologist, 0 to return to Main Menu.",
        "options": {
            "1": {"action": "end", "message": "Appointment booked with General Physician."},
            "2": {"action": "end", "message": "Appointment booked with Cardiologist."},
            "0": {"action": "goto", "target": "main"}
        }
    },

    "lab": {
        "prompt": "Press 1 to check lab report status, 0 to return to Main Menu.",
        "options": {
            "1": {"action": "end", "message": "Your lab report is ready for collection."},
            "0": {"action": "goto", "target": "main"}
        }
    },

    "billing": {
        "prompt": "Press 1 to know outstanding amount, 0 to return to Main Menu.",
        "options": {
            "1": {"action": "end", "message": "Your outstanding amount is 2500 rupees."},
            "0": {"action": "goto", "target": "main"}
        }
    }
}