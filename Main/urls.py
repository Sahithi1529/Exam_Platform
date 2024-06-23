from django.urls import path
from . import views

urlpatterns = [
    path('',views.returnHomePage),
    path('Assessments',views.returnAssessments),
    path('profile',views.returnProfile),
    path('performance',views.returnPerformance),
    path('doubtsolving',views.returnDoubts),
    path('studyguide',views.returnGuide)
]