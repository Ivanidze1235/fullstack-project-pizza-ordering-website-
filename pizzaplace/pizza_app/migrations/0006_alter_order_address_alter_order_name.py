# Generated by Django 4.2.18 on 2025-02-12 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0005_alter_order_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default='1, Main Street, Dublin', max_length=300),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(default='Name', max_length=50),
        ),
    ]
