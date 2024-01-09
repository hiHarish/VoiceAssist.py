# VoiceAssist.py
# It is basic python program for voice assistance.
# Python code for voice assistant:






import sys
import speech_recognition as sr
import pyttsx3
import subprocess
import webbrowser
import pywhatkit
import datetime
import pyaudio

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()

def greet():
    x='how I can assist you?'
    engine.say(x)
    engine.runAndWait()  
def cmd():
    with sr.Microphone() as source:
        print('Clearing background noise..Please wait')
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('Ask me anything..')
        recordedaudio=recognizer.listen(source)

    try:
        text=recognizer.recognize_google(recordedaudio,language='en_US')
        text=text.lower()
        print('Your message:',format(text))

    except Exception as ex:
        print(ex)
        sys.exit()

    if 'hello' in text:
        engine.say('hi, great to see you')
        engine.runAndWait()
    if 'chrome' in text:
        a='Opening chrome..'
        engine.say(a)
        engine.runAndWait()
        programName = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([programName])
    if 'time' in text:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()
    if 'play' in text:
        a='opening youtube..'
        engine.say(a)
        engine.runAndWait()
        pywhatkit.playonyt(text)
    if 'youtube' in text:
        b='opening youtube'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')
    if 'exit' in text:
        engine.say("thank you.., exiting.")
        engine.runAndWait()
        sys.exit()

greet()
while True:
    cmd()
