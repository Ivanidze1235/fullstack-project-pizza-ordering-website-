from django.db import models

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

    id = models.AutoField(primary_key=True)
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