from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sizes(models.Model):
    size = models.CharField(max_length=300)
    def __str__(self):
        return self.size
class Sauces(models.Model):
    sauce = models.CharField(max_length=300)
    def __str__(self):
        return self.sauce

class Cheeses(models.Model):
    cheese = models.CharField(max_length=300)
    def __str__(self):
        return self.cheese

class Pizza(models.Model):
    crust_choices = (
        ('Normal', 'Normal'),
        ('Thin', 'Thin'),
        ('Thick', 'Thick'),
        ('Gluten-free', 'Gluten-free'),
        ('Cardboard', 'Cardboard')
    )

    toppings_choices = (
        ('Pepperoni', 'Pepperoni'),
        ('Chicken', 'Chicken'),
        ('Ham', 'Ham'),
        ('Pineapple', 'Pineapple'),
        ('Peppers', 'Peppers'),
        ('Mushrooms', 'Mushrooms'),
        ('Onions', 'Onions')
    )
    user = models.CharField(default="none", max_length=100)

    size = models.CharField(max_length=300, default="", choices=[(si.size, si.size) for si in Sizes.objects.all()])
    sauce = models.CharField(max_length=300, default="", choices=[(sau.sauce, sau.sauce) for sau in Sauces.objects.all()])
    cheese = models.CharField(max_length=300, default="", choices=[(che.cheese, che.cheese) for che in Cheeses.objects.all()])    

    crust = models.CharField(max_length=300, choices=crust_choices, default="Normal")
    pepperoni = models.BooleanField(default=False)
    chicken = models.BooleanField(default=False)
    ham = models.BooleanField(default=False)
    pineapple = models.BooleanField(default=False)
    peppers = models.BooleanField(default=False)
    mushrooms = models.BooleanField(default=False)
    onions = models.BooleanField(default=False)