# Generated by Django 4.2.4 on 2023-10-12 08:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_alter_customuser_cpf_alter_customuser_data_nasc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oficina_1_disponivel', models.BooleanField(default=True)),
                ('oficina_2_disponivel', models.BooleanField(default=True)),
                ('oficina_3_disponivel', models.BooleanField(default=True)),
                ('data', models.DateField(default=datetime.datetime(2023, 10, 12, 8, 46, 52, 78331, tzinfo=datetime.timezone.utc), unique=True)),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cliente_Rquester', to='App.customuser')),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Car_Client', to='App.auto_register')),
            ],
        ),
        migrations.AddField(
            model_name='manutencion',
            name='Reserva_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Reserva', to='App.reserva'),
        ),
    ]