import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to greet
def greet():
    speak("Hello! How can I assist you today?")

# Function to get time
def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

# Function to get date
def get_date():
    current_date = datetime.date.today().strftime("%A, %B %d, %Y")
    speak(f"Today is {current_date}")

# Function to search the web
def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Here is what I found for {query} on the web.")

# Main function to process commands
def main():
    greet()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio).lower()

            print("You said:", command)

            if "hello" in command:
                greet()
            elif "time" in command:
                get_time()
            elif "date" in command:
                get_date()
            elif "search" in command:
                query = command.replace("search", "").strip()
                search_web(query)
            elif "exit" in command or "bye" in command:
                speak("Goodbye!")
                break
            else:
                speak("Sorry, I didn't catch that. Can you repeat?")
        
        except sr.UnknownValueError:
            print("Could not understand the audio")
            speak("Sorry, I didn't catch that. Can you repeat?")
        except sr.RequestError:
            print("Could not request results; check your internet connection")

if __name__ == "__main__":
    main()
