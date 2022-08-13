from django.db import models

# Create your models here.

class QrGenModel(models.Model):
    qr_name = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    color = models.CharField(max_length=15)


    def __str__(self):
        return f'{self.qr_name}, {self.link}, {self.color}'
    