# AI Accessibility Virtual Assistant

##  Overview

An AI-powered **Accessibility Virtual Assistant** designed to help users—especially individuals with disabilities—interact with their system using **voice and text commands**.
The assistant supports **adaptive behavior** using accessibility profiles and combines **offline logic with Generative AI** to ensure reliability even when AI services fail.

---

##  Key Features

*  Voice + ⌨️ Text interaction
*  Accessibility profiles (visual, hearing, cognitive)
*  Open/close system applications (Calculator, Notepad, Camera, etc.)
*  Camera control + photo capture using OpenCV
*  AI-powered answers using Gemini API
*  Offline fallback for basic queries
*  Context-aware command handling
*  Error handling + API failure fallback

---

##  System Architecture

```
User Input (Voice/Text)
        │
        ▼
Speech Recognition (if voice)
        │
        ▼
Input Processing
        │
        ├──▶ System Commands (open/close apps, camera)
        │
        ├──▶ Offline Responses (fast/local answers)
        │
        └──▶ AI Handler (Gemini API)
                     │
                     ▼
              Response Generation
                     │
                     ▼
        Output (Text / Voice via TTS)
```

---

## 📂 Project Structure

```
accessibility_assistant/
│
├── main.py                  # Main execution file
├── llm_handler.py           # Gemini AI integration
├── offline_responses.py     # Local fallback answers
├── system_commands.py       # OS/app control
├── camera_helper.py         # Camera + photo capture
├── context_manager.py       # Context tracking
├── accessibility_profile.py # User accessibility modes
├── tts_helper.py            # Text-to-speech
└── requirements.txt         # Dependencies
```

---

## ⚙️ Technologies Used

* Python
* SpeechRecognition (voice input)
* pyttsx3 / edge-tts (voice output)
* Webcam (camera handling)
* Google Gemini API (Generative AI)
* OS / subprocess / psutil (system control)

---

##  Setup Instructions

### 1️ Clone Project

```bash
git clone https://github.com/your-repo/accessibility-assistant.git
cd accessibility-assistant
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set API Key (IMPORTANT)

```powershell
$env:GOOGLE_API_KEY="YOUR_API_KEY"
```

### 5️⃣ Run Project

```bash
python app.py
```

---

## 🎮 Supported Commands

### 🔹 General

```
hello
what is time
what is today's date
```

### 🔹 Applications

```
open calculator
close calculator
open notepad
close notepad
```

### 🔹 Camera

```
open camera        → opens live camera
close camera       → closes camera
```

---

## 🧪 Example Run

```
You: open calculator
Assistant: Calculator opened.

You: what is AI
Assistant: AI is the simulation of human intelligence by machines.

You: take photo
Assistant: Photo saved successfully.
```

---

## 🧠 Accessibility Profiles

| Mode      | Input      | Output        |
| --------- | ---------- | ------------- |
| Visual    | Voice      | Voice         |
| Hearing   | Text       | Text          |
| Cognitive | Simplified | Slower speech |

---

## ⚠️ Limitations

* Gemini API free tier has **request limits**
* Requires microphone permissions for voice mode
* Works best on **Windows OS**

---

## 🚀 Future Enhancements

* GUI (Tkinter / Web UI)
* Wake word detection (“Hey Assistant”)
* Multi-language support
* Cloud-based user profiles

---

## 🏁 Conclusion

This project demonstrates how **Generative AI + Accessibility Design** can be combined to build inclusive systems that adapt to individual user needs while maintaining reliability through offline fallbacks.

---
