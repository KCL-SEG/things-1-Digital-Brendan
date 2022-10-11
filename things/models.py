import string
from tokenize import String
from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Thing(models.Model):
    name = models.TextField(unique=True, blank=False, max_length=30)
    description = models.TextField(unique=False, blank=True, max_length=120)
    quantity = models.PositiveIntegerField(unique=False, validators=[MaxValueValidator(100)])
