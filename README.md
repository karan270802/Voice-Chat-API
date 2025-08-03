# Voice Chat Assistant (Gemini)

A Python-based voice chat application that allows you to interact with Google's Gemini AI assistant using voice input and receives responses via text-to-speech.

## Features

- 🎤 **Voice Input**: Speak to the AI assistant using your microphone
- 🤖 **AI Integration**: Powered by Google's Gemini Pro
- 🔊 **Text-to-Speech**: AI responses are spoken back to you
- 💬 **Text Input**: Also supports typing messages
- 🎨 **Modern GUI**: Clean, intuitive interface built with tkinter
- ⏱️ **Real-time**: Live voice recognition and response

## Prerequisites

- Python 3.7 or higher
- Microphone access
- Speakers/headphones
- Google Gemini API key

## Installation

1. **Clone or download this repository**

2. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Gemini API key**:
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a `.env` file in the project directory
   - Add your API key:
     ```
     GEMINI_API_KEY=your_actual_api_key_here
     ```

## Usage

1. **Run the application**:
   ```bash
   python voice_chat_app.py
   ```

2. **Using Voice Input**:
   - Click the "🎤 Start Voice Input" button
   - Speak your message clearly
   - The app will automatically process your speech and get an AI response
   - The response will be displayed and spoken back to you

3. **Using Text Input**:
   - Type your message in the text field
   - Press Enter or click "Send"
   - The AI response will be displayed and spoken

## Troubleshooting

### PyAudio Installation Issues

If you encounter issues installing PyAudio:

**On macOS:**
```bash
brew install portaudio
pip install PyAudio
```

**On Ubuntu/Debian:**
```bash
sudo apt-get install python3-pyaudio portaudio19-dev
pip install PyAudio
```

**On Windows:**
```bash
pip install PyAudio
```

### Microphone Issues

- Ensure your microphone is properly connected and working
- Check system permissions for microphone access
- Try speaking clearly and in a quiet environment

### Gemini API Issues

- Verify your API key is correct in the `.env` file
- Ensure you have sufficient API credits
- Check your internet connection
- Make sure you're using a supported region for Gemini API

## Customization

You can customize the application by modifying:

- **Voice Settings**: Adjust speech rate and volume in the `VoiceChatApp` class
- **AI Model**: Change the Gemini model in the `__init__` method (e.g., 'gemini-pro-vision' for image support)
- **UI Colors**: Modify the color scheme in the `setup_ui` method
- **System Prompt**: Update the AI's behavior by modifying the initial message

## File Structure

```
Karan/
├── voice_chat_app.py      # Main application file
├── requirements.txt       # Python dependencies
├── env_example.txt        # Environment variables template
├── README.md             # This file
└── .env                  # Your API keys (create this)
```

## Dependencies

- `tkinter`: GUI framework (built-in with Python)
- `speech_recognition`: Voice recognition
- `pyttsx3`: Text-to-speech
- `google-generativeai`: Google Gemini API integration
- `python-dotenv`: Environment variable management
- `PyAudio`: Audio processing

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the application. 
1. **Run**:
   ```bash
   python voice_chat_api.py

