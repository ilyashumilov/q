from django.db import models

# Create your models here.

class number(models.Model):
    number = models.TextField(max_length=200)

