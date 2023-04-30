from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser

from django.db.models.deletion import SET_NULL
import os
import datetime

class User(AbstractUser):
    is_fuduser=models.BooleanField(default=False) 
    is_fudhotel=models.BooleanField(default=False) 
    is_fudadmin=models.BooleanField(default=False)

class HotProfile(models.Model):
    hname=models.CharField(max_length=250, null=True)
    place=models.CharField(max_length=250, null=True)
    adrss=models.CharField(max_length=250, null=True)
    email=models.CharField(max_length=250, null=True)
    mobs=models.TextField(max_length=10)
    hid=models.TextField(max_length=10)

