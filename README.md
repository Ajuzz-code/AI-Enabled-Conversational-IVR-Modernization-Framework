🏥 AI-Enabled Conversational IVR for Hospital Administration

An AI-enabled Interactive Voice Response (IVR) system designed for hospital administration to automate patient interactions such as appointment booking, lab report status, billing information, and reception support.

This project demonstrates how Conversational AI + IVR systems can modernize traditional phone-based hospital services using FastAPI, JavaScript, and Speech Recognition APIs.

📌 Project Overview

Hospitals receive a large number of calls for routine services such as:

Doctor appointment booking

Lab report status

Billing inquiries

Reception assistance

This project builds a web-based IVR simulator that allows patients to interact with hospital services using:

Keypad inputs

Voice commands

Conversational AI

The system processes user input and routes them to the appropriate hospital service automatically.

🚀 Features

✔ Interactive Hospital IVR Simulator
✔ Appointment Booking System
✔ Lab Report Status Inquiry
✔ Billing Information Retrieval
✔ Reception Assistance Option
✔ Voice Input using Web Speech API
✔ Conversational AI Intent Detection
✔ FastAPI Backend APIs
✔ Call Analytics Logging
✔ Agile Development Documentation

🧠 Conversational AI Capabilities

The IVR supports natural language interaction.

Example voice commands:

Book appointment
Check lab report
Billing information
Connect to reception

The system detects intent using keyword-based NLP and routes the request to the appropriate IVR menu.

🏗️ System Architecture
User (Browser / Voice Input)
        │
        ▼
Frontend IVR Simulator (HTML + JavaScript)
        │
        ▼
FastAPI Backend Server
        │
        ▼
Intent Detection Engine (ai_engine.py)
        │
        ▼
Menu Routing Middleware
        │
        ▼
Hospital Service Response
🛠️ Technologies Used
Technology	Purpose
Python	Backend development
FastAPI	REST API framework
JavaScript	Frontend interaction
HTML/CSS	IVR simulator UI
Web Speech API	Voice recognition
GitHub	Version control
Agile	Project management
📂 Project Structure
AI-Enabled-Conversational-IVR-Modernization-Framework
│
├── frontend
│   └── index.html
│
├── ai_engine.py
├── config.py
├── middleware.py
├── main.py
├── requirements.txt
│
├── agile_doc
│   ├── hospital_ivr_agile_template.xlsx
│   ├── hospital_ivr_defect_tracker.xlsx
│   └── hospital_ivr_unit_test_plan.xlsx
│
├── README.md
└── LICENSE

📊 Agile Project Documentation

The project follows Agile methodology.

Documentation files:

📄 Agile Template

📄 Defect Tracker

📄 Unit Test Plan

Located in:

agile_doc/
🧪 Example IVR Flow
Welcome to Care Hospital

Press 1 → Doctor Appointment
Press 2 → Lab Reports
Press 3 → Billing
Press 9 → Reception

Voice example:

User: "Book appointment"
System: "Appointment booked with General Physician"
📈 Future Enhancements

Integration with real hospital database

Speech-to-Text cloud APIs

Multi-language IVR support

Patient authentication

SMS notifications for appointments