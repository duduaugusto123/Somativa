# Generated by Django 4.2.4 on 2023-10-12 10:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_rename_data_reserva_data_reserva_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='data_reserva',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
