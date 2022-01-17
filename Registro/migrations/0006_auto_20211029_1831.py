# Generated by Django 3.2.6 on 2021-10-29 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0005_auto_20211029_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='created',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='updated',
        ),
        migrations.AddField(
            model_name='usuarios',
            name='creado',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='modificado',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
