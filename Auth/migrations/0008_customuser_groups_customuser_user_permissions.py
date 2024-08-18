# Generated by Django 5.1 on 2024-08-17 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0007_customuser_is_superuser'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='customuser_set', to='auth.group'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='customuser_permissions_set', to='auth.permission'),
        ),
    ]
