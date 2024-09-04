from django.db import models

# Create your models here.
from django.db import models

class MeowEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField
    description = models.TextField
    species = models.CharField(max_length=255)
    colour = models.CharField(max_length=255)
    age = models.IntegerField