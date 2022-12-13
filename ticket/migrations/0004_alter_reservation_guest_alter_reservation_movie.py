# Generated by Django 4.1.4 on 2022-12-12 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_alter_reservation_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reservation', to='ticket.guest'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reservation', to='ticket.movie'),
        ),
    ]
