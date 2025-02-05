from django.db import models

# Create your models here.

class Pizza(models.Model):
    size_choices = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )

    crust_choices = (
        ('N', 'Normal'),
        ('t', 'Thin'),
        ('T', 'Thick'),
        ('NG', 'Gluten-free'),
        ('C', 'Cardboard')
    )
    id = models.AutoField(primary_key=True)
    size = models.CharField(max_length=300, choices=size_choices, default="Small")
    crust = models.CharField(max_length=300, choices=crust_choices, default="Normal")
