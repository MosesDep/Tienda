# Generated by Django 3.2.6 on 2021-12-18 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lineas', '0003_remove_fotos_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='pictures',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('fotos', models.ImageField(blank=True, null=True, upload_to='fotolinea')),
                ('idnombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lineas.lineas')),
            ],
            options={
                'verbose_name': 'picture',
                'verbose_name_plural': 'pictures',
            },
        ),
    ]