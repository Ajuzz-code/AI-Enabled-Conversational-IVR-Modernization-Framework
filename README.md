# 🏥 AI-Enabled Conversational IVR for Hospital Administration

## 📌 Project Overview
---
This project implements a modern AI-enabled Interactive Voice Response (IVR) system for hospital administration.
It replaces traditional keypad-only IVR systems with a hybrid intelligent system that supports:

- 🔢 Keypad input (DTMF simulation)
- 🎤 Voice interaction (Speech Recognition)
- 💬 Conversational AI (multi-step dialogue)

The system allows patients to interact with hospital services like booking appointments, checking lab reports, and billing inquiries in a natural and user-friendly way.

---

## 🎯 Problem Statement

Hospitals receive a large number of repetitive calls for:

- Appointment booking
- Lab report status
- Billing inquiries
- Reception assistance

Traditional IVR systems are:

- ❌ Rigid (only keypad)
- ❌ Time-consuming
- ❌ Not user-friendly

👉 This project solves it using Conversational AI + IVR Hybrid System

---

## 🚀 Key Features
### 📞 IVR Simulator
- Real call simulation UI
- Full-screen calling experience
- Keypad interface
### 🤖 Conversational AI
- Understands natural language:
  - “Book appointment”
  - “Check lab report”
- Multi-step conversation:
  - Ask department → doctor → confirm
### 🎤 Voice Support
- Web Speech API integration
- Speak → system understands → responds
### 🏥 Appointment Booking
- Department selection:
  - General Physician
  - Cardiology
  - Neurology
  - Orthopedics
- Doctor selection with timing
- Confirmation system
### 🧪 Lab Report System
- Patient ID validation
- Personalized response:
  - Patient name
  - Available reports
- Detailed reports:
  - Blood test (Hemoglobin, Sugar, etc.)
  - X-Ray
  - Scan
### 🔁 Smart Navigation
- Switch between:
  - Voice
  - Text
  - Keypad
- Continue flow without reset
### 📊 Performance Testing
- Load testing using requests
- Measures API response time

---

## 🏗️ System Architecture


User (Voice / Text / Keypad)
│
▼
Frontend (HTML + JavaScript)
│
▼
FastAPI Backend
│
├── conversation_engine.py
├── ai_engine.py
├── middleware.py
│
▼
Hospital Services (Appointments / Lab / Billing)

---

## 🛠️ Technologies Used

| Technology        | Purpose                          |
|------------------|----------------------------------|
| Python           | Backend development              |
| FastAPI          | REST API framework               |
| JavaScript       | Frontend interaction             |
| HTML/CSS         | UI design                        |
| Web Speech API   | Voice recognition                |
| Requests         | Performance testing              |
| Uvicorn          | ASGI server                      |


---

## Advanced Features Implemented

- Hybrid IVR (Menu + Conversational AI)
- Voice + Text + Keypad integration
- State synchronization (conv_state + current_menu)
- Dynamic patient data handling
- Doctor availability with timing
- Real-time interaction simulation

---


## 📈 Future Enhancements
- 🔐 Patient authentication (OTP)
- 🌐 Multi-language support (Malayalam, Hindi)
- ☎️ Twilio real phone integration
- 🗄️ PostgreSQL database integration
- 📱 SMS/WhatsApp notifications
- 📊 Admin analytics dashboard

---


## 🎯 Conclusion

This project demonstrates how AI-powered IVR systems can modernize hospital administration by:

- Reducing manual workload
- Improving patient experience
- Enabling natural communication

It serves as a strong example of Conversational AI + IVR integration for real-world applications.

<<<<<<< HEAD
Deployed link : https://hospital-ivr.onrender.com
=======
Deployed link : [https://ai-enabled-conversational-ivr-xjac.onrender.com](https://hospital-ivr.onrender.com)
>>>>>>> 9ceacfd520d6ca12f0e1a5e719a2c21ca9a6725b

---

