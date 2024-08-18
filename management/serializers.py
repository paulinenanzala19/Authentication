
from rest_framework import serializers
from .models import Bus, Route, Schedule

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ['id', 'registration_number', 'capacity']

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'route_name']

class ScheduleSerializer(serializers.ModelSerializer):
    bus = BusSerializer()  # Nested serializer for Bus
    route = RouteSerializer()  # Nested serializer for Route

    class Meta:
        model = Schedule
        fields = ['id', 'bus', 'route', 'departure_time', 'arrival_time']
