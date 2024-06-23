from django.db import models

# Create your models here.
class User_Data(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(primary_key=True)
    phno = models.IntegerField(unique=True)
    password = models.CharField(max_length=20)


    

def __str__(self):
    return self.User_Data.username
def returnUsername(self):
    return self.username
def returnEmail(self):
    return self.email
def returnPhno(self):
    return self.phno
def returnPassword(self):
    return self.password 


