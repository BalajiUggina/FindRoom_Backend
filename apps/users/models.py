from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    # Choices for roles
    ROLE_CHOICES=(
        ('provider','Provider'),
        ('seeker','Seeker'),
        ('both','Both'),
    )
    #username=None to avoid username field in login
    username=None
    email=models.EmailField(unique=True)

    role=models.CharField(max_length=20,choices=ROLE_CHOICES)
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15,blank=True,null=True)
    gender=models.CharField(max_length=20,null=True,blank=True)
    occupation=models.CharField(max_length=50,blank=True,null=True)

    languages=models.JSONField(blank=True,null=True,default=list)

    # email based login
    USERNAME_FIELD='email'
    
    # only email+password for login 
    REQUIRED_FIELDS=[]

    def __str__(self):
        return f"{self.name}-{self.email}"
    
