# Generated by Django 3.2.6 on 2021-12-18 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Noticias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticias',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
