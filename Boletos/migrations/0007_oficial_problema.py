# Generated by Django 3.2.6 on 2021-12-27 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boletos', '0006_rename_correo_oficial_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='oficial',
            name='problema',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
