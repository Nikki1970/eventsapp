from django.shortcuts import render, redirect
from eventapp.models import Event, EventTime
from django.views import generic
from .forms import EventForm, EventTimeForm
from django.contrib.auth.models import User
from .filters import EventFilter,EventTimeFilter
from django.shortcuts import get_object_or_404
from django.forms import formset_factory, modelformset_factory
# Create your views here.


def index(request):
    total = Event.objects.all().count()
    context = {'total': total,}
    return render(request, 'index.html', context=context)


class EventDetailView(generic.DetailView):
    model = Event


def create_event(request):
    form = EventForm(request.POST or None)
    EventTimeFormSet = formset_factory(EventTimeForm, extra=2)
    eventtime_formset = EventTimeFormSet(request.POST or None)
    if form.is_valid() and eventtime_formset.is_valid():
        obj = form.save()
        for eventtimeform in eventtime_formset:
            eventtime = eventtimeform.save(commit=False)
            eventtime.event = obj
            eventtime.save()
        return redirect('list-of-events')

    return render(request, 'eventapp/event_edit.html',{'form': form, 'eventtime_formset':eventtime_formset})


def all_hosts(request):
    event = Event.objects.distinct('host')
    return render(request, 'eventapp/all_hosts.html', context={"all_events": event})


def host_events(request,inputhost):
    user = User.objects.get(username=inputhost)
    host = Event.objects.filter(host=user)
    return render(request, 'eventapp/host_events.html',context={"hosts":host})


def delete_event(request, pk):
    event = Event.objects.get(id=pk)
    if request.method =="POST":
        event.delete()
        return redirect('list-of-events')
    context = {'event':event}
    return render(request, "eventapp/delete.html",context)
    
def update_event(request,pk):
    event = Event.objects.get(id=pk)
    eventtime = event.eventtime_set.all()
    form = EventForm(request.POST or None, instance=event)
    EventTimeFormSet = modelformset_factory(model=EventTime, form=EventTimeForm, extra=1)
    eventtime_formset = EventTimeFormSet(request.POST or None, queryset=eventtime)
    if form.is_valid() and eventtime_formset.is_valid():
        obj = form.save()
        for eventform in eventtime_formset:
            eventtime = eventform.save(commit=False)
            eventtime.event = obj
            eventtime.save()
            return redirect('list-of-events')
    return render(request,"eventapp/event_edit.html",{'form': form, 'eventtime_formset':eventtime_formset})

def create_eventtime(request, pk):
    form = EventTimeForm(request.POST or None)
    if form.is_valid():
        eventtime = form.save(commit=False)
        eventtime.event = get_object_or_404(Event, pk=pk) 
        eventtime.save()
        return redirect('event-detail', pk=pk)
    return render(request, 'eventapp/event_time.html', {'form': form})

def filter_eventtime(request):
    eventtime = EventTimeFilter(request.GET, queryset=EventTime.objects.all())
    return render(request,'eventapp/event_timelist.html',{'filter': eventtime})