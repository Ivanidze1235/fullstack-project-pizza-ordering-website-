# Generated by Django 4.2.18 on 2025-02-12 12:10

from django.db import migrations, models
import pizza_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0006_alter_order_address_alter_order_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default='1, Main Street, Dublin', max_length=300, validators=[pizza_app.models.validate_address]),
        ),
    ]
