# Generated by Django 4.2.4 on 2023-10-10 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_auto_category_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cpf',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='data_nasc',
            field=models.DateField(blank=True, null=True),
        ),
    ]
