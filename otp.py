from twilio.rest import Client
import random
otp=random.randint(1000,9999)
print(otp)
acc='AC49f8b94428fcd4c755ff9aaaaed78d01'
auth='e4c02c92778057eb3ba02f84c40e549c'
client=Client(acc,auth)

message=client.messages.create(
    body='Hello is this vignesh ?Nenu ni collegemate' + str(otp),
    from_='+12136994692' ,
    to='+919652209108'
)
print(message.sid)