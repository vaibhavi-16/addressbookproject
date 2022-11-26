from django.db import models

# Create your models here.
class Address(models.Model):
    name = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    state = models.CharField(max_length=70)
    mbno = models.CharField(max_length=70)
