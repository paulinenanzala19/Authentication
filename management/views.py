from django.shortcuts import render
from .permissions import create_bus_perm,create_schedule_perm,create_route_perm
from rest_framework import generics,permissions
from .models import Bus, Route, Schedule
from .serializers import BusSerializer, RouteSerializer, ScheduleSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
import csv
from django.http import HttpResponse
from django.apps import apps

class BusListCreateView(generics.ListCreateAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    permission_classes=[permissions.AllowAny]

    def create_bus(request):
        if not request.user.has_perm('bus.can_create_bus'):
            return HttpResponseForbidden()

class RouteListCreateView(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes=[AllowAny]

    def create_bus(request):
        if not request.user.has_perm('route.can_create_route'):
            return HttpResponseForbidden()

class ScheduleListCreateView(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes=[AllowAny]

    def create_bus(request):
        if not request.user.has_perm('schedule.can_create_schedule'):
            return HttpResponseForbidden()

def export_model_to_csv(request, model_name):
    """
    Exports the data of a specified model to a CSV file.
    """
    try:
        model = apps.get_model('management', model_name)  
    except LookupError:
        return HttpResponse("Model not found", status=404)

    queryset = model.objects.all()  

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{model_name}.csv"'

    writer = csv.writer(response)
    
    # Write headers
    if model_name == 'Schedule':
        headers = ['Bus', 'Route', 'Departure Time', 'Arrival Time']
    else:
        headers = [field.name for field in model._meta.fields]
    writer.writerow(headers)
    
    # Write data rows
    for obj in queryset:
        if model_name == 'Schedule':
            row = [
                obj.bus.registration_number if obj.bus else '',
                f"{obj.route.route_name}" if obj.route else '',
                obj.departure_time,
                obj.arrival_time
            ]
        else:
            row = [getattr(obj, field.name) for field in model._meta.fields]
        writer.writerow(row)

    return response
