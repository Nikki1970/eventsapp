from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listofplaces/',views.PlacesListView.as_view(),name="list-of-places"),
    path('place/<int:pk>/', views.PlaceDetailView.as_view(), name='place-detail'),
    path('all_cities/', views.all_cities, name='all-cities'),
    path('city/places/<str:inputcity>/',views.city_places,name="city-places"),
    path('place/new/', views.place_new, name='place_new'),
]