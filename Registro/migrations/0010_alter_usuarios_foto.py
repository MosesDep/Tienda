# Generated by Django 3.2.6 on 2022-01-08 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0009_alter_usuarios_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='usuarios'),
        ),
    ]