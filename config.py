# config.py

MENUS = {

    "main": {
        "prompt": "Press 1 for Appointments\n2 for Lab Reports\n3 for Billing\n9 for Reception.",
        "options": {
            "1": {"action": "goto", "target": "appointments"},
            "2": {"action": "goto", "target": "lab"},
            "3": {"action": "goto", "target": "billing"},
            "9": {"action": "end", "message": "Connecting to Reception..."}
        }
    },

    # ---------------- APPOINTMENTS ----------------
    "appointments": {
    "prompt": "Press 1 General Physician\n2 Cardiologist\n3 Neurologist\n4 Orthopedic\n0 to return Main Menu.",
    "options": {
        "1": {"action": "goto", "target": "gp_doctors"},
        "2": {"action": "goto", "target": "cardio_doctors"},
        "3": {"action": "goto", "target": "neuro_doctors"},
        "4": {"action": "goto", "target": "ortho_doctors"},
        "0": {"action": "goto", "target": "main"}
        }
    },

    "gp_doctors": {
        "prompt": "Available Doctors:\n1. Dr Ravi - 10 AM to 12 PM\n2. Dr Meera -10 AM to 2 PM",
        "options": {
            "1": {"action": "confirm", "message": "Appointment booked with Dr Ravi at 10 AM"},
            "2": {"action": "confirm", "message": "Appointment booked with Dr Meera at 2 PM"}
        }
    },

    "cardio_doctors": {
        "prompt": "Available Cardiologists:\n1. Dr Arjun -11 AM to 1 PM\n2. Dr Sneha -4 PM to 8 PM",
        "options": {
            "1": {"action": "confirm", "message": "Appointment booked with Dr Arjun at 11 AM"},
            "2": {"action": "confirm", "message": "Appointment booked with Dr Sneha at 4 PM"}
        }
    },
    "neuro_doctors": {
    "prompt": "Available Neurologists:\n1. Dr Kiran - 12 PM to 4 PM\n2. Dr Anjali - 3 PM to 8 PM",
    "options": {
        "1": {"action": "confirm", "message": "Appointment booked with Dr Kiran at 12 PM."},
        "2": {"action": "confirm", "message": "Appointment booked with Dr Anjali at 3 PM."}
    }
},
"ortho_doctors": {
    "prompt": "Available Orthopedic Doctors:\n1. Dr Raj - 9 AM to 3 PM\n2. Dr Deepa - 5 PM to 10 PM",
    "options": {
        "1": {"action": "confirm", "message": "Appointment booked with Dr Raj at 9 AM."},
        "2": {"action": "confirm", "message": "Appointment booked with Dr Deepa at 5 PM."}
    }
},

    # ---------------- LAB MAIN ----------------
"lab": {
    "prompt": "Enter your Patient ID to check reports",
    "options": {
        "#": {"action": "goto", "target": "lab_menu"}
    }
},

# ---------------- LAB MENU ----------------
"lab_menu": {
    "prompt": "Select Report:\nPress 1 Blood Test\nPress 2 X-Ray\nPress 3 Scan report\nPress 0 Main Menu",
    "options": {
        "1": {"action": "goto", "target": "blood_report"},
        "2": {"action": "goto", "target": "xray_report"},
        "3": {"action": "goto", "target": "scan_report"},
        "0": {"action": "goto", "target": "main"}
    }
},

# ---------------- BLOOD ----------------
"blood_report": {
    "prompt": "Blood Report:\nStatus: Ready\nHemoglobin: Normal\nSugar: Normal\n\nDownload from hospital portal\nCheck other reports",
    "options": {
        "0": {"action": "goto", "target": "lab_menu"}
    }
},

# ---------------- XRAY ----------------
"xray_report": {
    "prompt": "X-Ray Report:\nStatus: Ready\nNo fracture detected\n\nCollect from hospital\nCheck other reports",
    "options": {
        "0": {"action": "goto", "target": "lab_menu"}
    }
},

# ---------------- SCAN ----------------
"scan_report": {
    "prompt": "Scan Report:\nStatus: Pending\nPlease check after 24 hours\nCheck other reports",
    "options": {
        "0": {"action": "goto", "target": "lab_menu"}
    }
},

    # ---------------- BILLING ----------------
    "billing": {
        "prompt": "Press 1 for amount\n0 to return.",
        "options": {
            "1": {"action": "end", "message": "Your bill is ₹2500"},
            "0": {"action": "goto", "target": "main"}
        }
    }
}
PATIENTS = {
    "1234": {
        "name": "Rahul",
        "blood": {
            "status": "Normal",
            "hemoglobin": "13.5 g/dL",
            "sugar": "95 mg/dL",
            "cholesterol": "Normal"
        },
        "xray": "No fracture",
        "scan": "Pending"
    },
    "5678": {
        "name": "Anjali",
        "blood": {
            "status": "High Sugar",
            "hemoglobin": "11.2 g/dL",
            "sugar": "180 mg/dL",
            "cholesterol": "High"
        },
        "xray": "Minor fracture",
        "scan": "Normal"
    }
}
