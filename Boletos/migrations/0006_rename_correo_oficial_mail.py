# Generated by Django 3.2.6 on 2021-12-27 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Boletos', '0005_auto_20211222_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oficial',
            old_name='correo',
            new_name='mail',
        ),
    ]