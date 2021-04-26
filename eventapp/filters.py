import django_filters
from django_filters import DateFilter
from .models import Event, EventTime

class EventFilter(django_filters.FilterSet):
    choice_day = tuple((x, x) for x in range(1, 32))
    choice_month = tuple((x, x) for x in range(1, 13))
    title = django_filters.CharFilter(lookup_expr='icontains')
    day = django_filters.ChoiceFilter(field_name="date",lookup_expr='day',label="Day",choices=choice_day)
    month = django_filters.ChoiceFilter(field_name='date', lookup_expr='month', label="Month",choices=choice_month)
    year = django_filters.NumberFilter(field_name='date', lookup_expr='year', label="Year")
    class Meta:
        model = Event
        fields = ['title','place','host']

class EventTimeFilter(django_filters.FilterSet):
    choice_day = tuple((x, x) for x in range(1, 32))
    choice_month = tuple((x, x) for x in range(1, 13))
    event = django_filters.CharFilter(field_name = 'event__title',lookup_expr='icontains',label="Event Title")
    day = django_filters.ChoiceFilter(field_name="date",lookup_expr='day',label="Event Day",choices=choice_day)
    month = django_filters.ChoiceFilter(field_name='date', lookup_expr='month', label="Event Month",choices=choice_month)
    year = django_filters.NumberFilter(field_name='date', lookup_expr='year', label="Event Year")
    class Meta:
        model = EventTime
        fields = ['day','month','year','starttime','endtime']

