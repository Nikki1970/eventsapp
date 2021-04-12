from django.shortcuts import render, redirect
from placesapp.models import Place
from django.views import generic
from .forms import PlaceForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    num = Place.objects.all().count()
    context = {'num': num}
    return render(request, 'index.html', context=context)

class PlacesListView(generic.ListView):
    model = Place

class PlaceDetailView(generic.DetailView):
    model = Place

def all_cities(request):
    place = Place.objects.distinct('city')
    return render(request, 'placesapp/all_cities.html', context={"all_places": place})

def city_places(request,inputcity):
    city = Place.objects.filter(city=inputcity)
    return render(request,'placesapp/city_places.html',context={"cities":city})
    
def place_new(request):
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.save()
            return redirect('list-of-places')
    else:
        form = PlaceForm()
    return render(request, 'placesapp/place_edit.html', {'form': form})