from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
     dob=models.CharField(max_length=20,default=0)