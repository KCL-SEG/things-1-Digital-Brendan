import string
from tokenize import String
from django.db import models

# Create your models here.
class Thing(models.Model):
    name = ""
    description = ""
    quantity = int()
