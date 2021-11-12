from tkinter import *
from tkinter import messagebox
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia as w
a=sr.Recognizer()
root=Tk()
root.title("Browser")
b=pyttsx3.init()
f=open("1.txt","a")
def audio():
    n=name.get()
    b.say("hello {} welcome to  your browser".format(n))
    b.runAndWait()
    f.write(n)
    messagebox.showinfo('The app is under construction')
    b.say("Hello     good   morning    This    is   your   private   browser")
    b.runAndWait()
    lab3=Label(root,text="At present  your   browser  can perform wikipedia operations and youtube operations")
    lab3.pack()
    b.say("Whatsapp service will be available soon")
    b.runAndWait()
    b.say("Enter 1 for youtube and 2 for wikipedia services ")
    b.runAndWait()
    l=Label(root,text="Enter the option: ")
    l.pack()
    op=Entry(root)
    op.pack()
    """but=Button(root,text="Next")
    but.pack()"""
    """#if(option==1):
        speech()
    elif(option==2):"""
    wiki()
def wiki():
    b.say("Please tell the topic name: ")
    b.runAndWait()
    with sr.Microphone() as source:
        audio=a.listen(source)  
        text=a.recognize_google(audio)
    result=w.summary(text,5)
    lc=Label(root,text=result)
    lc.pack()
    b.say(result)
    b.runAndWait()  
def speech():
    b.say("speak")
    b.runAndWait()
    try:
        with sr.Microphone() as source:
            audio=a.listen(source)
            text=a.recognize_google(audio)
            f.write(text)
            f.close()
            pywhatkit.playonyt(text)
    except:
        b.say("say the name in a clear manner")
        b.runAndWait()
        messagebox.showerror('speak clearly')
root.maxsize(800,800)
root.minsize(500,500)
root.config(bg='yellow')
label1=Label(root,text="Browser for you",font=('sansserif',20,'bold'),borderwidth="15")
label1.pack()
#labw=Label(root,text="Wikipedia search",font=('sansserif',20,"bold"),borderwidth="15")
#labw.pack()
lab2=Label(root,text="Enter your name: ")
lab2.pack()
name=Entry(root)
name.pack()
button=Button(root,text="Click to start your Browser",command=audio)
button.pack(padx=90,pady=90)
root.mainloop()
#how to play youtube videos in tkinter 