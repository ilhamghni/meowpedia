import uuid
from django.db import models
from django.contrib.auth.models import User

class CatEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    age = models.IntegerField()
    description = models.TextField()
    species = models.CharField(max_length=255)
    colour = models.CharField(max_length=255)
