# Generated by Django 4.2.2 on 2023-07-04 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['titulo', 'editorial', 'status']},
        ),
    ]