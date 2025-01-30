from django.db import models

# Create your models here.

class Pizza(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    ingredients = models.TextField()