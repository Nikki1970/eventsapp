from django.shortcuts import render, redirect
from eventapp.models import Event, EventTime
from django.views import generic
from .forms import EventForm
from django.contrib.auth.models import User
from .filters import EventFilter
# Create your views here.


def index(request):
    total = Event.objects.all().count()
    context = {'total': total,}
    return render(request, 'index.html', context=context)

class EventListView(generic.ListView):
    model = Event
    template_name = 'eventsapp/event_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EventFilter(self.request.GET,queryset=self.get_queryset())
        return context
class EventDetailView(generic.DetailView):
    model = Event

def new_event(request):
    form = EventForm
    return render(request,)

def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('list-of-events')
    else:
        form = EventForm()
    return render(request, 'eventapp/event_edit.html', {'form': form})

def all_hosts(request):
    event = Event.objects.distinct('host')
    return render(request, 'eventapp/all_hosts.html', context={"all_events": event})

def host_events(request,inputhost):
    user = User.objects.get(username=inputhost)
    host = Event.objects.filter(host=user)
    return render(request, 'eventapp/host_events.html',context={"hosts":host})

def deleteEvent(request, pk):
    event = Event.objects.get(id=pk)
    if request.method =="POST":
        event.delete()
        return redirect('list-of-events')
    context = {'event':event}
    return render(request, "eventapp/delete.html",context)

def updateEvent(request, pk):
    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)
    if request.method == "POST":
        form = EventForm(request.POST,instance=event)
        if form.is_valid():
            form.save()
            return redirect('list-of-events')
    context = {'form':form}
    return render(request,"eventapp/event_edit.html",context)