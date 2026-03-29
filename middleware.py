from config import MENUS,PATIENTS

def process_menu(session, digit):

   
    current_menu = session["current_menu"]
    menu = MENUS[current_menu]
    
    
     # ✅ LAB PATIENT ID HANDLING
    if current_menu == "lab":
        patient_id = digit
         # ❌ INVALID ID
        if patient_id not in PATIENTS:
            return {
                "status": "invalid",
                "prompt": "Invalid Patient ID. Try again."
            }
        
        session["patient_id"] = patient_id
        session["current_menu"] = "lab_menu"
        name = PATIENTS[patient_id]["name"]

        return {
            "status": "ok",
            "menu": "lab_menu",
            "prompt": f"Welcome {name}\n\n" + MENUS["lab_menu"]["prompt"]
        }
    
           # ---------------- BLOOD REPORT ----------------
    if current_menu == "blood_report":
        if "patient_id" not in session:
            session["current_menu"] = "lab"
            return {
                "status": "invalid",
                "prompt": "Please enter Patient ID first"
            }
       
         # ✅ allow navigation
        if digit == "0":
            session["current_menu"] = "lab_menu"
            return {"status": "ok", "menu": "lab_menu", "prompt": MENUS["lab_menu"]["prompt"]}
        if digit == "2":
            session["current_menu"] = "xray_report"
            return process_menu(session, "2")
        if digit == "3":
            session["current_menu"] = "scan_report"
            return process_menu(session, "3")
        patient = PATIENTS[session["patient_id"]]
        return {
            "status": "ok",
            #"menu": "lab_menu",
            "prompt": f"Blood Report for {patient['name']}:\nStatus: {patient['blood']}\n\nPress 2 X-Ray\nPress 3 Scan report\nCheck other reports"
            }

    # ---------------- XRAY ----------------
    if current_menu == "xray_report":
        if "patient_id" not in session:
            session["current_menu"] = "lab"
            return {
                "status": "invalid",
                "prompt": "Please enter Patient ID first"
            }
        patient = PATIENTS[session["patient_id"]]
        if digit == "0":
            session["current_menu"] = "lab_menu"
            return {"status": "ok", "menu": "lab_menu", "prompt": MENUS["lab_menu"]["prompt"]}
        if digit == "1":
            session["current_menu"] = "blood_report"
            return process_menu(session, "1")
        if digit == "3":
            session["current_menu"] = "scan_report"
            return process_menu(session, "3")
        patient = PATIENTS[session["patient_id"]]
        return {
            "status": "ok",
            #"menu": "lab_menu",
             "prompt": f"X-Ray Report for {patient['name']}:\n{patient['xray']}\n\nPress 1 Blood test\nPress 3 Scan report\nCheck other reports"
        }

    # ---------------- SCAN ----------------
    if current_menu == "scan_report":
        if "patient_id" not in session:
            session["current_menu"] = "lab"
            return {
                "status": "invalid",
                "prompt": "Please enter Patient ID first"
            }
        

        patient = PATIENTS[session["patient_id"]]
        if digit == "0":
            session["current_menu"] = "lab_menu"
            return {"status": "ok", "menu": "lab_menu", "prompt": MENUS["lab_menu"]["prompt"]}
        if digit == "1":
            session["current_menu"] = "blood_report"
            return process_menu(session, "1")
        if digit == "2":
            session["current_menu"] = "xray_report"
            return process_menu(session, "2") 
        patient = PATIENTS[session["patient_id"]]

        return {
            "status": "ok",
            "prompt": f"Scan Report for {patient['name']}:\n{patient['scan']}\n\nCheck other reports"
        } 

   

    if digit not in menu["options"]:
        return {"status": "invalid", "prompt": menu["prompt"]}

    option = menu["options"][digit]
    action = option["action"]

    # ✅ GOTO (ONLY HERE target EXISTS)
    if action == "goto":

        target = option["target"]   # ✅ define here

        session["current_menu"] = target

        # ✅ STORE DEPARTMENT HERE ONLY
        if target == "gp_doctors":
            session["department"] = "General Physician"

        elif target == "cardio_doctors":
            session["department"] = "Cardiology"

        elif target == "neuro_doctors":
            session["department"] = "Neurology"

        elif target == "ortho_doctors":
            session["department"] = "Orthopedics"

        return {
            "status": "ok",
            "menu": target,
            "prompt": MENUS[target]["prompt"]
        }

    # ✅ CONFIRM
    if action == "confirm":

        session["doctor"] = option["message"]
        session["current_menu"] = "main"

        return {
            "status": "ok",
            "menu": "main",
            "prompt": option["message"] 
                      #"\n\nPress 1 General Physician, 2 Cardiologist, 3 Neurologist, 4 Orthopedic, 0 to return Main Menu."
        }

    # ✅ END
    if action == "end":
        return {
            "status": "hangup",
            "message": option["message"]
        }