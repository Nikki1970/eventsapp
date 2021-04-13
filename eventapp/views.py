from django.shortcuts import render
from eventapp.models import Event
from django.views import generic
# Create your views here.


def index(request):
    total = Event.objects.all().count()
    context = {'total': total,}
    return render(request, 'index.html', context=context)

class EventListView(generic.ListView):
    model = Event

class EventDetailView(generic.DetailView):
    model = Event