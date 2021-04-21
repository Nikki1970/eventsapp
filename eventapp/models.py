from django.db import models
from placesapp.models import Place
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from datetime import date
from django.utils import timezone
from model_utils.models import TimeStampedModel
from django.urls import reverse

class Event(TimeStampedModel):
    title = models.CharField(max_length = 12,help_text="Event Name")
    place = models.ForeignKey(Place,on_delete=models.SET_NULL,null=True,blank=True)
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tags = TaggableManager()

    def __str__(self):
        return '{0}'.format(self.title,self.host)
    
    def get_absolute_url(self):
        return reverse('event-detail',args=[str(self.id)])

class EventTime(models.Model):
    event = models.ForeignKey('Event',on_delete=models.SET_NULL,null=True)
    date = models.DateField(default=date.today,null=True)
    starttime = models.TimeField(blank=True,null=True)
    endtime = models.TimeField(blank=True,null=True)

    def __str__(self):
        return str(self.date)