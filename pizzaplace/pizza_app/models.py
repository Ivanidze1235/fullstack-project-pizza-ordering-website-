from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime

# Create your models here.

def validate_card(value):
    if len(value) != 16 or not str.isdigit(value):
        raise ValidationError("Card number should be 16 digits long and a number.")

def validate_cvv(value):
    if len(value) != 3 or not str.isdigit(value):
        raise ValidationError("Cvv should be 3 digits long and a number.")

def validate_date(value):
    if value < datetime.date.today():
        raise ValidationError("Card expired.")

def validate_address(value):
    if value == "":
        raise ValidationError("Empty address.")


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

    size = models.ForeignKey(Sizes, on_delete=models.CASCADE, default=1)
    crust = models.CharField(max_length=300, choices=crust_choices, default="Normal")
    sauce = models.ForeignKey(Sauces, on_delete=models.CASCADE, default=1)
    cheese = models.ForeignKey(Cheeses, on_delete=models.CASCADE, default=1)
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
    name = models.CharField(max_length=50, default="Name")
    address = models.CharField(max_length=300, default="1, Main Street, Dublin", validators=[validate_address])
    card_number = models.CharField(max_length=16, default="0000000000000000", validators=[validate_card])
    exp_date = models.DateField(default=datetime.date.today, validators=[validate_date])
    cvv = models.CharField(max_length=3, default="000", validators=[validate_cvv])
