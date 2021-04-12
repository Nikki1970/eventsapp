from django.db import models
from placesapp.models import Place
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from datetime import date
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length = 12,help_text="Event Name")
    place = models.ForeignKey(Place,on_delete=models.SET_NULL,null=True,blank=True)
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tags = TaggableManager()
    eventtime = models.DateTimeField(default=timezone.now,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} {1}'.format(self.title,self.host)