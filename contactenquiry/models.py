from django.db import models

# Create your models here.

class contactenquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=50)
    message = models.TextField()