from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# 0x57A900137C83472EdE10690720df8f9b15D0c70f

class User(AbstractUser):
    public_key = models.CharField(max_length=128)
    image = models.ImageField(upload_to="profile_pictures")
    citizenship_number = models.CharField(max_length=100)

class Voter(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL)

    #TODO: Property Name will be computed from blockchain

class Candidate(models.Model):
    user = models.OneToOneField(User, null=True,blank=True,on_delete=models.SET_NULL)

    #TODO: Name and vot4es will be computed from blockchain.

class ElectionManager(models.Model):
    user = models.OneToOneField(User, null=True,blank=True,on_delete=models.SET_NULL)

    #TODO: elections and other infos will be added here.

