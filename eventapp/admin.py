from django.contrib import admin
from .models import Event, EventTime
# Register your models here.

class EventTimeInline(admin.TabularInline):
    model = EventTime
    extra = 3

class EventAdmin(admin.ModelAdmin):
    inlines = [EventTimeInline]

admin.site.register(Event, EventAdmin)