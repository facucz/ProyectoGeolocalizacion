from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Entry

@admin.register(Entry)
class EntryAdmin(OSMGeoAdmin):
    default_lon = -6566652.48306
    default_lat = -3180550.76859
    default_zoom = 12

    