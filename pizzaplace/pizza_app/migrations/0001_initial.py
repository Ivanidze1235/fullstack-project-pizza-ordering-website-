# Generated by Django 4.2.18 on 2025-02-07 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cheeses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cheese', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('size', models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], default='Small', max_length=300)),
                ('crust', models.CharField(choices=[('Normal', 'Normal'), ('Thin', 'Thin'), ('Thick', 'Thick'), ('Gluten-free', 'Gluten-free'), ('Cardboard', 'Cardboard')], default='Normal', max_length=300)),
                ('sauce', models.CharField(choices=[('Tomato', 'Tomato'), ('BBQ', 'BBQ'), ('Mayonnaise', 'Mayonnaise')], default='Tomato', max_length=300)),
                ('cheese', models.CharField(choices=[('Mozzarella', 'Mozzarella'), ('Cheddar', 'Cheddar'), ('Vegan', 'Vegan'), ('Low fat', 'Low fat')], default='Cheddar', max_length=300)),
                ('pepperoni', models.BooleanField(default=False)),
                ('chicken', models.BooleanField(default=False)),
                ('ham', models.BooleanField(default=False)),
                ('pineapple', models.BooleanField(default=False)),
                ('peppers', models.BooleanField(default=False)),
                ('mushrooms', models.BooleanField(default=False)),
                ('onions', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Sauces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sauce', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=300)),
            ],
        ),
    ]
