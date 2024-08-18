from django.contrib import admin
from .models import Bus, Route,Schedule

# Register your models here.
admin.site.register(Bus)
admin.site.register(Route)
# admin.site.register(Schedule)

from django.contrib import admin
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect


def export_as_csv(modeladmin, request, queryset):
    model_name = queryset.model._meta.model_name
    url = reverse('export_model_to_csv', args=[model_name])
    return HttpResponseRedirect(url)

export_as_csv.short_description = "Export as CSV"

@admin.register(Schedule)  # Replace with your model
class ScheduleAdmin(admin.ModelAdmin):
    actions = [export_as_csv]
