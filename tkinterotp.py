from tkinter import *
from tkinter import messagebox
from twilio.rest import Client
import random as r
import pyttsx3 as p
root=Tk()
root.title("login page")
root.maxsize(900,900)
root.minsize(600,600)
root.configure(bg='skyblue')
def verify_otp():
    namei=names.get()
    phi=ph.get()
    global otp
    otp=r.randint(1000,9999)
    print(otp)
    account='AC83bb1669c93cd18c5573f0b452de1786'
    auth_key='632100376efbb223ef53b4541aeec5c8'
    client=Client(account,auth_key)
    message=client.messages.create(
        body='Hello' + str(namei) + 'with'+str(phi) + 'your otp is '+str(otp) ,
        from_='+15706164176',
        to='+919392642428' 
    )
    print(message.sid)
def verify():
    f=ot.get()
    if(f==otp):
        messagebox.showinfo('LOGIN SUCCESSFUL')
    else:
        messagebox.showwarning('wrong otp')





lab1=Label(text="Login System using Otp",font=('sansserif','25','bold'),bg="lightpink",fg='black')
lab1.pack()
lab=Frame(height='3',width='1000',borderwidth='5',bg="Blue")
lab.pack()
name=Label(text="Name of the Account : ",font=('sanserif','20',"bold"))
name.pack(padx=50,pady=45)
names=Entry(root)
names.pack()
phc=Label(text="Mobile number: ",font=('sansserif','20','bold'))
phc.pack(padx=50,pady=75)
ph=Entry(root)
ph.pack()
engine=p.init()
engine.say("Welcome to login system please enter the name of the account and the Mobile number ")
engine.runAndWait()
sub=Button(root,text="Send otp",command=verify_otp)
sub.pack(padx=50,pady=85)
olab3=Label(root,text="Enter the otp")
olab3.pack(padx=50,pady=65)
ot=Entry(root)
ot.pack(padx=50,pady=67)
st=Button(root,text="Submit",command="verify")
st.pack()
root.mainloop()