from django.urls import path
from . import views
from django_filters.views import FilterView
from eventapp.models import Event
urlpatterns = [
    path('', views.index, name='eventindex'),
    # path('listofevents/',views.EventListView.as_view(),name="list-of-events"),
    path('event/<int:pk>/',views.EventDetailView.as_view(), name="event-detail"),
    path('event/new/',views.create_event, name='new_event'),
    path('all_hosts/', views.all_hosts, name='all-hosts'),
    path('event/host/<str:inputhost>/',views.host_events, name="host-events"),
    path('delete_event/<int:pk>/',views.delete_event, name="delete_event"),
    path('update_event/<int:pk>/',views.update_event, name="update_event"),
    path('event/timings/<int:pk>/',views.create_eventtime, name="eventtime_new"),
    path('event/timefilter/',views.filter_eventtime, name="filter"),
    path('list/',FilterView.as_view(model = Event, filterset_fields=('title','place','host'), template_name='eventapp/event_list.html'), name="list-of-events"),
]