# Generated by Django 4.1.4 on 2023-01-18 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0010_alter_reservation_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticket.movie'),
        ),
    ]
