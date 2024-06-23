from django.shortcuts import render
from django.http import HttpResponse
from django.db import models

# Create your views here.

#Assessments
def returnAssessments(request):
    return render(request,"Assessments.html")

#Profile
def returnProfile(request):
    #return render(request,"Profile.html")
    return render(request,"Profile.html")

#Dashboard
def returnPerformance(request):
    #return render(request,"Dashboard.html")
    return HttpResponse("Dashboard")

#Doubts
def returnDoubts(request):
    #return render(request,"Doubts.html")
    return HttpResponse("Doubt Solving")

#StudyGuide
def returnGuide(request):
    #return render(request,"Guide.html")
    return HttpResponse("Study Guide")


#HomePage
def returnHomePage(request):
    return render(request,"Home.html")
   
  
     
         