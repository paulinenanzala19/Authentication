from django.shortcuts import render
from django.contrib.auth.models import Permission
from .models import Bus, Route,Schedule
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group


create_bus_perm = Permission.objects.get_or_create(
    codename='can_create_bus',
    name='Can create bus',
    content_type=ContentType.objects.get_for_model(Bus)
)[0]
create_schedule_perm = Permission.objects.get_or_create(
    codename='can_create_schedule',
    name='Can create schedule',
    content_type=ContentType.objects.get_for_model(Schedule)
)[0]
create_route_perm = Permission.objects.get_or_create(
    codename='can_create_route',
    name='Can create route',
    content_type=ContentType.objects.get_for_model(Route)
)[0]

admin_group, created = Group.objects.get_or_create(name='admin')
admin_group.permissions.add(create_bus_perm, create_route_perm, create_schedule_perm)