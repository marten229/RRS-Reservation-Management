# Generated by Django 5.0.6 on 2024-06-16 14:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationManagement', '0011_alter_reservation_buchungsuhrzeit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='buchungsuhrzeit',
            field=models.TimeField(default=datetime.time(14, 21, 44, 367796)),
        ),
    ]
