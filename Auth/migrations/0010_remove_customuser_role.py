# Generated by Django 4.1.13 on 2024-08-18 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0009_customuser_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='role',
        ),
    ]
