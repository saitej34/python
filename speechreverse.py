#recognises our voice and repeats it
import speech_recognition as sr
import pyttsx3 as p
import wikipedia
import pywhatkit
a=sr.Recognizer()
engine=p.init()

with sr.Microphone() as source:
    print("speak")
    audio=a.listen(source)
    text=a.recognize_google(audio)
    print(text)
    engine.say(text)
    engine.runAndWait()
    pywhatkit.playonyt(text)


