# Generated by Django 4.0.5 on 2023-07-14 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='categoria',
            field=models.CharField(blank=True, choices=[('P', 'Particular'), ('T', 'Transporte'), ('C', 'Carga')], default='P', max_length=20),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='marca',
            field=models.CharField(blank=True, choices=[('1', 'Fiat'), ('2', 'Chevrolet'), ('3', 'Ford'), ('4', 'Toyota')], default='3', max_length=20),
        ),
    ]
