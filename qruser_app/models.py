from django.db import models

# Create your models here.
class QrSaver(models.Model):
    owner = models.CharField(max_length=100)
    qrname = models.CharField(max_length=100)
    qrlink = models.CharField(max_length=150)