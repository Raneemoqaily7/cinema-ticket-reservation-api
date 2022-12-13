# Generated by Django 4.1.4 on 2022-12-12 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_guest_movie_reservation_delete_box'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='ticket.movie'),
        ),
    ]
