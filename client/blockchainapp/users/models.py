from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# 0x57A900137C83472EdE10690720df8f9b15D0c70f

class User(AbstractUser):
    public_key = models.CharField(max_length=128)
    image = models.ImageField(upload_to="profile_pictures",null=True,blank=True)
    citizenship_number = models.CharField(max_length=100)


    @property
    def isvoter(self):
        return hasattr(self, 'voter')

    @property
    def iscandidate(self):
        return hasattr(self, 'candidate')

    @property
    def ismanager(self):
        return hasattr(self, 'electionmanager')

class Voter(models.Model):
    elections = models.ManyToManyField('voting.Election')
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.user.username + " | Voter"

    #TODO: Property Name will be computed from blockchain

class Candidate(models.Model):
    elections = models.ManyToManyField('voting.Election')
    user = models.OneToOneField(User, null=True,blank=True,on_delete=models.SET_NULL)
    #votes <- blockchain


    @property
    def votes(self):
        return 1337

    def __str__(self):
        return self.user.username + " | Candidate"

    #TODO: Name and vot4es will be computed from blockchain.

class ElectionManager(models.Model):
    user = models.OneToOneField(User, null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username + " | Manager"

    #TODO: elections and other infos will be added here.

