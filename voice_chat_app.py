
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import speech_recognition as sr
import pyttsx3
import threading
import google.genai as genai
import os
from dotenv import load_dotenv
import queue
import time

# Load environment variables
load_dotenv()

class VoiceChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Chat Assistant (Gemini)")
        self.root.geometry("800x600")
        self.root.configure(bg='#2c3e50')
        
        # Initialize components
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.microphone = sr.Microphone()
        
        # Configure Gemini
        # genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        self.client = genai.Client()
       
        # Voice settings
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)
        
        # Threading
        self.recording = False
        self.message_queue = queue.Queue()
        
        self.setup_ui()
        self.setup_voice_thread()
        
    def setup_ui(self):
        """Setup the user interface"""
        # Main frame
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="Voice Chat Assistant (Gemini)", 
            font=("Arial", 24, "bold"),
            fg='#ecf0f1',
            bg='#2c3e50'
        )
        title_label.pack(pady=(0, 20))
        
        # Chat display area
        chat_frame = tk.Frame(main_frame, bg='#34495e')
        chat_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame,
            wrap=tk.WORD,
            font=("Arial", 12),
            bg='#34495e',
            fg='#ecf0f1',
            insertbackground='#ecf0f1',
            state=tk.DISABLED
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Control buttons frame
        button_frame = tk.Frame(main_frame, bg='#2c3e50')
        button_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Voice button
        self.voice_button = tk.Button(
            button_frame,
            text="🎤 Start Voice Input",
            font=("Arial", 14, "bold"),
            bg='#e74c3c',
            fg='white',
            command=self.toggle_voice_recording,
            relief=tk.FLAT,
            padx=20,
            pady=10
        )
        self.voice_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # Text input
        self.text_input = tk.Entry(
            button_frame,
            font=("Arial", 12),
            bg='#34495e',
            fg='#ecf0f1',
            insertbackground='#ecf0f1',
            relief=tk.FLAT
        )
        self.text_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.text_input.bind('<Return>', self.send_text_message)
        
        # Send button
        send_button = tk.Button(
            button_frame,
            text="Send",
            font=("Arial", 12, "bold"),
            bg='#3498db',
            fg='white',
            command=self.send_text_message,
            relief=tk.FLAT,
            padx=15,
            pady=5
        )
        send_button.pack(side=tk.RIGHT)
        
        # Status label
        self.status_label = tk.Label(
            main_frame,
            text="Ready to chat! Click the microphone or type a message.",
            font=("Arial", 10),
            fg='#bdc3c7',
            bg='#2c3e50'
        )
        self.status_label.pack()
        
        # Add initial message
        self.add_message("Assistant", "Hello! I'm your Gemini-powered voice chat assistant. You can speak to me or type your messages.")
        
    def setup_voice_thread(self):
        """Setup voice recognition thread"""
        def voice_listener():
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                
            while True:
                if self.recording:
                    try:
                        with self.microphone as source:
                            self.root.after(0, lambda: self.status_label.config(text="Listening... Speak now!"))
                            audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                            
                        self.root.after(0, lambda: self.status_label.config(text="Processing speech..."))
                        
                        # Recognize speech
                        text = self.recognizer.recognize_google(audio)
                        self.message_queue.put(("user", text))
                        
                    except sr.WaitTimeoutError:
                        self.root.after(0, lambda: self.status_label.config(text="No speech detected. Try again."))
                    except sr.UnknownValueError:
                        self.root.after(0, lambda: self.status_label.config(text="Could not understand audio. Try again."))
                    except sr.RequestError as e:
                        self.root.after(0, lambda: self.status_label.config(text=f"Error with speech recognition: {e}"))
                    except Exception as e:
                        self.root.after(0, lambda: self.status_label.config(text=f"Error: {e}"))
                    
                    self.recording = False
                    self.root.after(0, self.update_voice_button)
                    self.root.after(0, lambda: self.status_label.config(text="Ready to chat! Click the microphone or type a message."))
                
                time.sleep(0.1)
        
        # Start voice thread
        voice_thread = threading.Thread(target=voice_listener, daemon=True)
        voice_thread.start()
        
        # Start message processing thread
        def process_messages():
            while True:
                try:
                    sender, message = self.message_queue.get(timeout=0.1)
                    if sender == "user":
                        self.root.after(0, lambda: self.handle_user_message(message))
                except queue.Empty:
                    continue
        
        message_thread = threading.Thread(target=process_messages, daemon=True)
        message_thread.start()
    
    def toggle_voice_recording(self):
        """Toggle voice recording on/off"""
        if not self.recording:
            self.recording = True
            self.update_voice_button()
            self.status_label.config(text="Starting voice input...")
        else:
            self.recording = False
            self.update_voice_button()
            self.status_label.config(text="Voice input stopped.")
    
    def update_voice_button(self):
        """Update voice button appearance"""
        if self.recording:
            self.voice_button.config(text="⏹️ Stop Recording", bg='#e67e22')
        else:
            self.voice_button.config(text="🎤 Start Voice Input", bg='#e74c3c')
    
    def send_text_message(self, event=None):
        """Send text message"""
        message = self.text_input.get().strip()
        if message:
            self.text_input.delete(0, tk.END)
            self.handle_user_message(message)
    
    def handle_user_message(self, message):
        """Handle user message and get AI response"""
        self.add_message("You", message)

        # Get AI response using the new client
        try:
            response = self.client.models.generate_content(model='gemini-1.5-flash-latest', contents=message)
            ai_response = response.text
            self.add_message("Assistant", ai_response)

            # Speak the response
            threading.Thread(target=self.speak_text, args=(ai_response,), daemon=True).start()

        except Exception as e:
            error_msg = f"Error getting response: {str(e)}"
            self.add_message("System", error_msg)
            messagebox.showerror("Error", error_msg)
    
    def add_message(self, sender, message):
        """Add message to chat display"""
        self.chat_display.config(state=tk.NORMAL)
        
        # Add timestamp
        timestamp = time.strftime("%H:%M:%S")
        
        # Format message
        if sender == "You":
            self.chat_display.insert(tk.END, f"[{timestamp}] {sender}: {message}\n", "user")
        elif sender == "Assistant":
            self.chat_display.insert(tk.END, f"[{timestamp}] {sender}: {message}\n", "assistant")
        else:
            self.chat_display.insert(tk.END, f"[{timestamp}] {sender}: {message}\n", "system")
        
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
        
        # Configure tags for different message types
        self.chat_display.tag_config("user", foreground="#3498db")
        self.chat_display.tag_config("assistant", foreground="#2ecc71")
        self.chat_display.tag_config("system", foreground="#e74c3c")
    
    def speak_text(self, text):
        """Speak the given text"""
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error speaking text: {e}")

def main():
    # Check for Gemini API key
    if not os.getenv('GEMINI_API_KEY'):
        print("Error: GEMINI_API_KEY not found in environment variables.")
        print("Please create a .env file with your Gemini API key:")
        print("GEMINI_API_KEY=your_gemini_api_key_here")
        print("\nGet your API key from: https://makersuite.google.com/app/apikey")
        return
    
    root = tk.Tk()
    app = VoiceChatApp(root)
    
    # Handle window close
    def on_closing():
        app.recording = False
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main() 