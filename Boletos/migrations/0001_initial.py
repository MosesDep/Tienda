# Generated by Django 3.2.6 on 2021-12-16 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Registro', '0007_remove_usuarios_modificado'),
    ]

    operations = [
        migrations.CreateModel(
            name='boletos',
            fields=[
                ('destino', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('precio', models.FloatField()),
                ('salida', models.DateField()),
                ('llegada', models.DateField()),
                ('created', models.DateField(auto_now=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='boletos')),
            ],
            options={
                'verbose_name': 'boleto',
                'verbose_name_plural': 'boletos',
            },
        ),
        migrations.CreateModel(
            name='fotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fotos', models.ImageField(blank=True, null=True, upload_to='paisajes')),
                ('iddestino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Boletos.boletos')),
            ],
            options={
                'verbose_name': 'foto',
                'verbose_name_plural': 'fotos',
            },
        ),
        migrations.CreateModel(
            name='compra',
            fields=[
                ('DD', models.AutoField(primary_key=True, serialize=False)),
                ('precio', models.FloatField()),
                ('cantidad', models.PositiveIntegerField()),
                ('producto', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(auto_now=True, null=True)),
                ('iduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro.usuarios')),
            ],
            options={
                'verbose_name': 'compra',
                'verbose_name_plural': 'compras',
            },
        ),
    ]
