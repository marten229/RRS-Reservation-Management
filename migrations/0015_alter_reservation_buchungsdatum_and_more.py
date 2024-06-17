# Generated by Django 5.0.6 on 2024-06-17 10:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationManagement', '0014_alter_reservation_buchungsuhrzeit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='buchungsdatum',
            field=models.DateField(default=datetime.date(2024, 6, 17)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='buchungsuhrzeit',
            field=models.TimeField(default=datetime.time(10, 54, 5, 68735)),
        ),
    ]
