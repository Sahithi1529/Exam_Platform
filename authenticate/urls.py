from django.urls import path
from . import views 

urlpatterns = [
    path("Signup",views.returnSignupPage),
    path("Signin",views.returnSigninPage),
    path("OTP",views.returnOTP),
    path("VerifyEmail",views.returnVerifyEmail),
    path("Home",views.returnHome),
    path("LoginType",views.returnType),
    path("Tsignin",views.user_type_teacher)
    
]
