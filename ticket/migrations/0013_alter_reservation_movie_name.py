# Generated by Django 4.1.4 on 2023-01-18 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0012_reservation_movie_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='movie_name',
            field=models.CharField(max_length=30),
        ),
    ]
