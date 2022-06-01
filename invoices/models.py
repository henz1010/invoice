from django.db import models
from profiles.models import Profile
from receivers.models import Receiver

# Create your models here.


class Invoice(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE)
