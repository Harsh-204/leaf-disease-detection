# 🌿 Leaf Disease Detection System

[![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1-009688.svg?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg?style=flat&logo=streamlit)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776ab.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/Groq-AI%20Powered-orange.svg?style=flat)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat)](LICENSE)

An enterprise-grade, AI-powered leaf disease detection system featuring a clean dual-interface architecture: a **FastAPI backend service** and an interactive, highly-polished **Streamlit web application**. Built with Meta's Llama Vision models via the fast Groq API, this application provides accurate disease identification, severity assessment, and actionable treatment recommendations for agricultural and horticultural applications.

## 🎯 Key Features

- **📸 Live Camera Capture & Upload**: Directly analyze your plant's health using your device's camera for instant results or upload any high-resolution image!
- **🦠 Advanced Disease Detection**: Identifies 500+ plant diseases (fungal, bacterial, viral, pest-related) and smartly flags invalid scans (e.g. non-plant items).
- **📊 Precision Severity Assessment**: AI-powered classification of disease severity levels with visual confidence percentage meters (0-100%).
- **💡 Expert Treatment Recommendations**: Comprehensive symptom breakdown, causal analysis, and step-by-step treatment protocols.
- **⚡ Real-time Processing**: Sub-5-second analysis response times using Groq API ecosystem.
- **🌟 Premium UI**: A highly polished, responsive interface with glassmorphism, animated result cards, and dynamic visual indicators.

## 🏗️ Project Architecture

**Main Application Components:**
- **`Leaf Disease/main.py`** - Core AI Detection Engine integrating Groq's Llama Vision API, parsing JSON outputs, managing Base64 encodings, and robust error handling.
- **`app.py`** - FastAPI Backend Service with REST API endpoint handling `/disease-detection-file` requests.
- **`main.py`** - Streamlit Web Application rendering the interactive UI, drag-and-drop features, camera inputs, and dynamic results layout.
- **`utils.py`** - Helper utilities for system functionality.

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.8+
- Groq API Key ([Get your free key here](https://console.groq.com/))

### 1. Repository Setup
Clone the repository:
```bash
git clone https://github.com/Harsh-204/leaf-disease-detection.git
cd leaf-disease-detection
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a `.env` file in the project's root with the following variable:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Running the Application Locally
You need to launch both the backend (FastAPI) and the frontend (Streamlit) services. 

**Terminal 1: Launch the Backend (FastAPI)**
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2: Launch the Frontend (Streamlit)**
```bash
streamlit run main.py --server.port 8501 --server.address 0.0.0.0
```
Open your browser and navigate to `http://localhost:8501`. Provide an image or use your camera to see the diagnostics!

## 🤝 Contributing
Contributions are more than welcome. Please fork the repository, create a separate branch for your feature, and submit a pull request for review.

## 📝 License
This project is licensed under the **MIT License**. See the `LICENSE` file for details.

### Support
- Project by [@Harsh-204](https://github.com/Harsh-204)
- Have an issue? Feel free to open a ticket in the GitHub issue tracker.

---

<div align="center">
<b>🌱 Empowering Agriculture Through AI-Driven Plant Health Solutions 🌱</b>
</div>
