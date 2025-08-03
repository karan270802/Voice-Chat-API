# Voice-Chat-API

# Voice-Chat-API

## 🧠 Real-Time AI Assistant

This is a real-time AI assistant built using **Python**, **tkinter**, and the **Google Gemini API**. The application supports natural language conversations and provides real-time search functionality for up-to-date responses.

---

## ✨ Features

- **🖼️ Interactive GUI**: Built using tkinter with a clean and user-friendly interface.
- **🔗 Gemini API Integration**: Utilizes Google's **Gemini 1.5 Flash** model for fast, intelligent replies.
- **🌐 Real-Time Search**: Detects keywords like "weather", "news", or "latest" to fetch up-to-date information using a search API.
- **💬 Streaming Responses**: Dynamically streams the AI's replies chunk by chunk for an engaging experience.
- **⚙️ Multi-threaded**: Non-blocking architecture ensures the interface remains responsive during AI processing.

---

## 🎥 Demonstration

📺 **Video Walkthrough**: Watch a demo of the AI Assistant.  
Replace `YOUR_VIDEO_ID` below with the actual ID:

https://www.youtube.com/watch?v=YOUR_VIDEO_ID

yaml
Copy
Edit

---

## 🚀 Getting Started

Follow the steps below to run the project on your local machine.

### ✅ Prerequisites

- Python 3.6 or above
- `pip` installed

---

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/karan270802/Voice-Chat-API.git
   cd Voice-Chat-API
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
🔑 Configuration
The application needs API keys for:

Google Gemini API

Google Custom Search API

🔐 Note: For simplicity, API keys are hardcoded (but using environment variables is recommended for production).

Open voice_chat_api.py in a text editor.

In the __init__ method, replace:

python
Copy
Edit
gemini_api_key = "YOUR_GEMINI_API_KEY_HERE"
In the perform_realtime_search method, replace:

python
Copy
Edit
search_api_key = "YOUR_GOOGLE_CUSTOM_SEARCH_API_KEY"
search_engine_id = "YOUR_SEARCH_ENGINE_ID"
▶️ Running the Application
bash
Copy
Edit
python voice_chat_api.py
💡 Usage
Chat Normally: Type a message and click "Send" or press Enter to talk with the AI.

Ask for Live Info: Use keywords like "weather", "latest news", "headlines", etc., and the app will fetch real-time information using the search API.

🗂️ Project Structure
bash
Copy
Edit
Voice-Chat-API/
├── voice_chat_api.py       # Main application logic
├── requirements.txt        # Python dependencies
└── .gitignore              # Files to be ignored by Git
🛠️ Technologies Used
Python – Core language

tkinter – GUI framework

google-generativeai – Gemini API integration

requests – For HTTP API calls

Google Custom Search API – For real-time search capabilities

