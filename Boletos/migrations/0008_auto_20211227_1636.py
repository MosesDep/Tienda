# Generated by Django 3.2.6 on 2021-12-27 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Boletos', '0007_oficial_problema'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oficial',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='oficial',
            name='problema',
        ),
    ]
