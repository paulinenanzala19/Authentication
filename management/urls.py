from django.urls import path
from .views import BusListCreateView, RouteListCreateView, ScheduleListCreateView, export_model_to_csv


urlpatterns = [
    path('buses/', BusListCreateView.as_view(), name='bus-list-create'),
    path('routes/', RouteListCreateView.as_view(), name='route-list-create'),
    path('schedules/', ScheduleListCreateView.as_view(), name='schedule-list-create'),
    path('export/<str:model_name>/', export_model_to_csv, name='export_model_to_csv'),

]