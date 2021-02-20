from django.db import models
from users.models import Candidate, Voter
# Create your models here.
class Election(models.Model):
    region = models.CharField(max_length=255)
    expiry_date = models.DateField()


# class Vote(models.Model):
#     candidate = models.ForeignKey(Candidate, on_delete=models.SET_NULL)
#     voter = models.ForeignKey(Voter, on_delete=models.SET_NULL)
#     election = models.ForeignKey(Election, on_delete=models.CASCADE)