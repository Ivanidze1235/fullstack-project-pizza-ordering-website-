# Generated by Django 4.2.18 on 2025-02-09 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default='A place far-far away...', max_length=50),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pizza_app.sizes'),
        ),
    ]
