# Generated by Django 4.0.5 on 2023-07-14 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0002_alter_vehiculo_categoria_alter_vehiculo_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='categoria',
            field=models.CharField(blank=True, choices=[('Particular', 'Particular'), ('Transporte', 'Transporte'), ('Carga', 'Carga')], default='P', max_length=20),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='marca',
            field=models.CharField(blank=True, choices=[('Fiat', 'Fiat'), ('Chevrolet', 'Chevrolet'), ('Ford', 'Ford'), ('Toyota', 'Toyota')], default='Ford', max_length=20),
        ),
    ]
