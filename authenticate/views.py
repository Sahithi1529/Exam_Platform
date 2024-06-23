from django.shortcuts import render,redirect
from . import models
from django.http import HttpResponse
import smtplib
import random
from email.message import EmailMessage

class Refer:
      email = None
      phno = None
      username = None
      password = None
      role = None

#Landing Page
def LandingPage(request):
    return render(request,"Landing.html")

#Signup Page
def returnSignupPage(request):
          return render(request,"Signup.html")

#Signin Page
def returnSigninPage(request):
          return render(request,"Signin.html")    

#LoginType
def returnType(request):
      return render(request,"LoginType.html")  

#Choosing
def user_type_teacher(request):
      return  render(request,"Tsignin.html")
    #return HttpResponse("User not found!!")                       


#Choosing
def user_type_student(request):
      return  render(request,"Signin.html")
    #return HttpResponse("User not found!!")                       



#HomePage
def returnHome(request):
      if request.method=="POST":          
            entered_email = request.POST.get('email')
            entered_password = request.POST.get('password')
            try:
                  result = models.User_Data.objects.get(email=entered_email)
                  password = result.password
                  if(entered_password == password): 
                        return redirect("/Home")
            except:
                  return HttpResponse("Unexpected error Occured!!")
              

#Generating OTP
def generate_otp():
      otp=""
      for i in range(4):
        otp += str(random.randint(0,9))
      return otp  


#Sending OTP to Email
def sendEmail(user_mail,otp):
      server  = smtplib.SMTP("smtp.gmail.com",587)
      server.starttls()
      server.login('examvisionn@gmail.com','gnir zssh fnrj rlws')
      msg = EmailMessage()
      msg['Subject'] = "OTP Verification"
      msg['From'] = 'examvisionn@gmail.com'
      msg['To'] = user_mail 
      msg.set_content("Welcome to Exam Vision Platform\n Your OTP is:"+str(otp) )
      server.send_message(msg)
      server.quit()
       

#EnteringOTP
def returnOTP(request):
           if request.method=="POST":
              entered_email = request.POST.get("email")
              Refer.phno = request.POST.get("phno")
              Refer.username = request.POST.get("username")
              Refer.password = request.POST.get("password")
              Refer.email = entered_email
              user_mail = entered_email 
              obj = generate_otp()
              sendEmail(user_mail,obj)
              request.session['otp'] = obj
              return render(request,"OTP.html")
           else:
                return HttpResponse("Unexpected error Occured!!")
                  

#VerifyEmail
def returnVerifyEmail(request):
       if request.method=="POST":
              first_digit = request.POST.get("one")
              second_digit = request.POST.get("two")
              third_digit = request.POST.get("three")
              fourth_digit = request.POST.get("four")
              entered_OTP = str(first_digit+second_digit+third_digit+fourth_digit)
              generated_OTP = request.session.get('otp')
              if entered_OTP == generated_OTP:
                    username = Refer.username
                    email = Refer.email
                    phno = Refer.phno
                    password = Refer.password
                    
                    print("EMAIL:"+email)
                    row = models.User_Data(username = username,email = email,phno = phno,password = password)
                    row.save()  
                    return render(request,"Signin.html")   
              else:
                    return HttpResponse("Wrong OTP Entered")
                     
                     
                     



    
           



