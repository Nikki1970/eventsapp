from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='eventindex'),
    path('listofevents/',views.EventListView.as_view(),name="list-of-events"),
    path('event/<int:pk>/',views.EventDetailView.as_view(),name="event-detail"),
    path('event/new/',views.event_new,name='new_event'),
    path('all_hosts/', views.all_hosts, name='all-hosts'),
    path('event/host/<str:inputhost>/',views.host_events, name="host-events"),
    path('delete_event/<int:pk>/',views.deleteEvent, name="delete_event"),
    path('update_event/<int:pk>/',views.updateEvent, name="update_event"),
    path('event/timings/<int:pk>/',views.eventtime_new, name="eventtime_new"),
]