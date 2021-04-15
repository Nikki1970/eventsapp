import django_filters
from django_filters import DateFilter
from .models import Event

class EventFilter(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = ['title','place','host']

