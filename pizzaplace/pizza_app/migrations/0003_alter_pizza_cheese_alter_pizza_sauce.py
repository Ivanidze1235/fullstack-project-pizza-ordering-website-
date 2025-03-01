# Generated by Django 4.2.18 on 2025-02-09 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0002_alter_order_address_alter_pizza_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='cheese',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pizza_app.cheeses'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='sauce',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pizza_app.sauces'),
        ),
    ]
