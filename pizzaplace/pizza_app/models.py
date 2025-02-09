from django.db import models
from django.contrib.auth.models import User
import datetime

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

    size = models.ForeignKey(Sizes, on_delete=models.CASCADE, null=True)
    crust = models.CharField(max_length=300, choices=crust_choices, default="Normal")
    sauce = models.ForeignKey(Sauces, on_delete=models.CASCADE, null=True)
    cheese = models.ForeignKey(Cheeses, on_delete=models.CASCADE, null=True)
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
