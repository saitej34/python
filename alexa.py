import pywhatkit
import speech_recognition as sr
import pyttsx3

a=sr.Recognizer()
b=sr.Recognizer()

d=pyttsx3.init()
d.say("Hello    i  am    your     personal assistant  alexa   your    entertainment    helper!   how    can  i  help   you?")
d.runAndWait()

print("speak with alexa.Alexa can play music for you")
with sr.Microphone() as source:
    print("speak now....")
    audio=a.listen(source)
    text=a.recognize_google(audio)
    d.say("good morning")
    d.runAndWait()
    with sr.Microphone() as source1:
        print("speak out song name")
        r=b.listen(source1)
        text2=b.recognize_google(r)
        d.say("opening your song details")
        d.runAndWait()
        pywhatkit.playonyt(text2)

