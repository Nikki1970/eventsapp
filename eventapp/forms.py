from django import forms
from .models import Event, EventTime

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title','place','host','tags')

class EventTimeForm(forms.ModelForm):

    class Meta:
        model = EventTime
        fields = ('date','starttime','endtime')