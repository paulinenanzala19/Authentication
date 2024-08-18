# Generated by Django 5.1 on 2024-08-17 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0008_customuser_groups_customuser_user_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('DRIVER', 'Driver'), ('CUSTOMER', 'Customer')], default='CUSTOMER', max_length=10),
        ),
    ]
