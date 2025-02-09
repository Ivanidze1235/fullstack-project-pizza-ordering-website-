from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Sizes(models.Model):
    size = models.CharField(max_length=300)

class Sauces(models.Model):
    sauce = models.CharField(max_length=300)

class Cheeses(models.Model):
    cheese = models.CharField(max_length=300)

class Pizza(models.Model):
    size_choices = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large')
    )

    crust_choices = (
        ('Normal', 'Normal'),
        ('Thin', 'Thin'),
        ('Thick', 'Thick'),
        ('Gluten-free', 'Gluten-free'),
        ('Cardboard', 'Cardboard')
    )

    sauce_choices = (
        ('Tomato', 'Tomato'),
        ('BBQ', 'BBQ'),
        ('Mayonnaise', 'Mayonnaise')
    )

    cheese_choices = (
        ('Mozzarella', 'Mozzarella'),
        ('Cheddar', 'Cheddar'),
        ('Vegan', 'Vegan'),
        ('Low fat', 'Low fat')
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

    size = models.CharField(max_length=300, choices=size_choices, default="Small")
    crust = models.CharField(max_length=300, choices=crust_choices, default="Normal")
    sauce = models.CharField(max_length=300, choices=sauce_choices, default="Tomato")
    cheese = models.CharField(max_length=300, choices=cheese_choices, default="Cheddar")
    pepperoni = models.BooleanField(default=False)
    chicken = models.BooleanField(default=False)
    ham = models.BooleanField(default=False)
    pineapple = models.BooleanField(default=False)
    peppers = models.BooleanField(default=False)
    mushrooms = models.BooleanField(default=False)
    onions = models.BooleanField(default=False)

class Order(models.Model):
    usr = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    pizza = models.ForeignKey(Pizza, on_delete=models.PROTECT, blank=True, null=True)
    date = models.DateField(auto_now=True)
    name = models.CharField(max_length=50, default="joe")
    address = models.CharField(max_length=50, default="Negra Arroyo lane")
    card_number = models.CharField(max_length=16, default="0000000000000000")
    exp_date = models.DateField(default=datetime.date.today)
    cvv = models.CharField(max_length=3, default="000")
