# Generated by Django 4.2.2 on 2023-07-06 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_book_preferencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='preferencia',
            field=models.CharField(blank=True, choices=[('A', 'Azul'), ('N', 'Negro'), ('B', 'Blanco'), ('G', 'Gris')], default='', max_length=200),
        ),
    ]
