# Generated by Django 4.1.13 on 2024-08-19 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_remove_schedule_arrival_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='arrival_time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]
