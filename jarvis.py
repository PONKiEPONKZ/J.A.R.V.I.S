import speech_recognition as sr
import pyttsx3
import subprocess
from langdetect import detect

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the speech recognizer
r = sr.Recognizer()

# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to execute the command
def execute_command(command):
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        print("Error executing command:", e)

# Main loop
while True:
    # Listen for voice input
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        # Convert speech to text
        command = r.recognize_google(audio)
        print("You said:", command)

        # Detect the language of the command
        language = detect(command)

        # Perform NLP on the command based on the detected language
        if language == "nl":
            # Process the command as Dutch
            execute_command(f"xdg-open {command}")  # Replace with appropriate Dutch command handling
        else:
            # Process the command as English
            execute_command(f"xdg-open {command}")  # Replace with appropriate English command handling

    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service:", e)
