# Generated by Django 3.2.6 on 2022-01-01 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Boletos', '0011_tabla'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oficial',
            name='iduser',
        ),
        migrations.DeleteModel(
            name='compra',
        ),
        migrations.DeleteModel(
            name='oficial',
        ),
    ]
