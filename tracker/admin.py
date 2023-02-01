from django.contrib import admin
from .models import Measurement


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ("user", "id", "type", "date", "value")
    list_filter = ("user",)
