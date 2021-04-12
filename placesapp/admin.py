from django.contrib import admin
from .models import Place
from django.contrib.gis.admin import OSMGeoAdmin
# Register your models here.
admin.site.register(Place)
