from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class QrGenModel(models.Model):
    qr_name = models.CharField(max_length=14)
    link = models.CharField(max_length=100)
    color = models.CharField(max_length=15)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.qr_name}, {self.link}, {self.color}'
    