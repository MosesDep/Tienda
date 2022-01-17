# Generated by Django 3.2.6 on 2021-10-04 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Registro', '0004_usuarios_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='prediccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultado', models.FloatField()),
                ('iduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro.usuarios')),
            ],
            options={
                'verbose_name': 'prediccion',
                'verbose_name_plural': 'predicciones',
            },
        ),
    ]
