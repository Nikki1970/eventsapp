from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='eventindex'),
    path('listofevents/',views.EventListView.as_view(),name="list-of-events"),
]