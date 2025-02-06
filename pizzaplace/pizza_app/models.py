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

    sauce_choices = (
        ('T', 'Tomato'),
        ('B', 'BBQ'),
        ('M', 'Mayonnaise')
    )

    cheese_choices = (
        ('M', 'Mozzarella'),
        ('C', 'Cheddar'),
        ('V', 'Vegan'),
        ('L', 'Low fat')
    )

    toppings_choices = (
        ('P', 'Pepperoni'),
        ('C', 'Chicken'),
        ('H', 'Ham'),
        ('Pa', 'Pinapple'),
        ('Pp', 'Peppers'),
        ('M', 'Mushrooms'),
        ('O', 'Onions')
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