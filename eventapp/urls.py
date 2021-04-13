from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='eventindex'),
    path('listofevents/',views.EventListView.as_view(),name="list-of-events"),
    path('event/<int:pk>/',views.EventDetailView.as_view(),name="event-detail"),
    path('event/new/',views.event_new,name='new_event')
]