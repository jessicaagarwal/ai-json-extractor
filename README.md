# 🔍 AI JSON Extractor using Streamlit & Groq API (Ongoing Project)

An **AI-powered JSON extraction tool** built with **Streamlit** and **Groq API**, leveraging **LLaMA-3 models**. This app can extract structured data like **Name, Email, Phone, or custom fields** from unstructured text or uploaded files.

---

## 🚀 Live Demo
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-json-extractor-jesstesting.streamlit.app/)

---

## ✨ Features  
- ✅ Extract structured data from **unstructured text**
- ✅ **Dynamic fields** – Choose what fields you want in the JSON
- ✅ **Download JSON** output in one click 
- ✅ **File Upload Support** – TXT & PDF extraction 
- ✅ **Secure API key handling** via `.env` or Streamlit Secrets 
- ✅ Handles **invalid JSON** gracefully  
- ✅ Powered by **Groq API** using `llama-3.3-70b-versatile`

---

## 🛠 Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python
- **LLM Provider:** Groq API

---

## 📂 Project Structure
```
├── app.py
├── README.md
├── requirements.txt
└── .env.example
```

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/jessicaagarwal/ai-json-extractor.git
cd ai-json-extractor
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate   # On Mac/Linux
.venv\Scripts\activate      # On Windows
```

---


## 🔑 API Setup

### 1. Get Groq API Key
- Visit [Groq Console](https://console.groq.com/keys)
- Copy your API key

### 2. Local Development
Create `.env` file in project root:
```
GROQ_API_KEY=your_api_key_here
```

Install dependencies:
```
pip install -r requirements.txt
```

Run the app:
```
streamlit run app.py
```

### 3. Streamlit Cloud Deployment
- Add your key in **Streamlit Secrets**:
```
GROQ_API_KEY="your_api_key_here"
```

---


## ✅ requirements.txt
```
streamlit
python-dotenv
groq
pdfplumber
httpx==0.27.0
```

---

## ▶️ Run the App
```bash
streamlit run app.py
```

The app will be available at:
```
http://localhost:8501
```

---

## 📚 Resources
- [Groq API Docs](https://console.groq.com/docs)
- [Streamlit Docs](https://docs.streamlit.io)

---

## 🔥 Future Enhancements
- Add **history of extractions**
- Support for **multiple file uploads**
- Add **image-to-text (OCR)** for scanned PDFs
- Add Multi-LLM Support (OpenAI, Claude, Gemini)

---

### ⭐ If you like this project, give it a star on GitHub!
