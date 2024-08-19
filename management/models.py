from django.db import models
from django.contrib.auth.models import User
from datetime import time


class Bus(models.Model):
    bus_number = models.CharField(max_length=10, unique=True)
    capacity = models.PositiveIntegerField()
    registration_number = models.CharField(max_length=20, unique=True)


    def __str__(self):
        return self.registration_number

class Route(models.Model):
    route_name = models.CharField(max_length=100)

    def __str__(self):
        return self.route_name

class Schedule(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    departure_time = models.TimeField()
    arrival_time = models.TimeField(default=time(0, 0, 0))

    def __str__(self):
        return f"{self.bus} - {self.route} - {self.departure_time}"
