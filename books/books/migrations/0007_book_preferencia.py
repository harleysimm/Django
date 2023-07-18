# Generated by Django 4.2.2 on 2023-07-04 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_book_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='preferencia',
            field=models.CharField(blank=True, choices=[('A', 'Azul'), ('N', 'Negro'), ('B', 'Blanco'), ('G', 'Gris')], max_length=1),
        ),
    ]