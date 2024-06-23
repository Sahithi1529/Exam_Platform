'''import random
import smtplib
from email.message import EmailMessage
from . import views

otp=""
for i in range(4):
    otp += str(random.randint(0,9))

server  = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login('examvisionn@gmail.com','gnir zssh fnrj rlws')

msg = EmailMessage()
msg['Subject'] = "OTP Verification"
msg['From'] = 'examvisionn@gmail.com'
msg['To'] = user_mail
msg.set_content("Welcome to Exam Vision Platform\n Your OTP is:"+str(otp) )

server.send_message(msg)

print("Email Sent")'''