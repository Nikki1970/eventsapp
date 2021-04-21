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

class EventListView(generic.ListView):
    model = Event
    template_name = 'eventsapp/event_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EventFilter(self.request.GET,queryset=self.get_queryset())
        return context

class EventDetailView(generic.DetailView):
    model = Event

def event_new(request):
    form = EventForm(request.POST or None)
    EventTimeFormSet = formset_factory(EventTimeForm, extra=2)
    eventtime_formset = EventTimeFormSet(request.POST or None)
    if form.is_valid() and eventtime_formset.is_valid():
        form = form.save()
        for eventform in eventtime_formset:
            eventform = eventform.save(commit=False)
            eventform.event = form
            eventform.save()
        return redirect('list-of-events')

    return render(request, 'eventapp/event_edit.html',{'form': form, 'eventtime_formset':eventtime_formset})

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

# def updateEvent(request, pk):
#     event = Event.objects.get(id=pk)
#     form = EventForm(instance=event)
#     if request.method == "POST":
#         form = EventForm(request.POST,instance=event)
#         if form.is_valid():
#             form.save()
#             return redirect('list-of-events')
#     context = {'form':form}
#     return render(request,"eventapp/event_edit.html",context)

def updateEvent(request,pk):
    event = Event.objects.get(id=pk)
    eventtime = event.eventtime_set.all()
    form = EventForm(request.POST or None, instance=event)
    EventTimeFormSet = modelformset_factory(model=EventTime, form=EventTimeForm, extra=1)
    eventtime_formset = EventTimeFormSet(request.POST or None, queryset=eventtime)
    if form.is_valid() and eventtime_formset.is_valid():
        form = form.save()
        for eventform in eventtime_formset:
            eventform = eventform.save(commit=False)
            eventform.event = form
            eventform.save()
            return redirect('list-of-events')
    return render(request,"eventapp/event_edit.html",{'form': form, 'eventtime_formset':eventtime_formset})

def eventtime_new(request, pk):
    form = EventTimeForm(request.POST or None)
    if form.is_valid():
        event_form = form.save(commit=False)
        event_form.event = get_object_or_404(Event, pk=pk) 
        event_form.save()
        return redirect('event-detail', pk=pk)
    return render(request, 'eventapp/event_time.html', {'form': form})

def eventtimefilter(request):
    eventtime = EventTimeFilter(request.GET, queryset=EventTime.objects.all())
    return render(request,'eventapp/event_timelist.html',{'filter': eventtime})