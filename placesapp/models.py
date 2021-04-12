from django.db import models
from django.contrib.gis.db.models import PointField
from django.urls import reverse
# Create your models here.

class Place(models.Model):
    title = models.CharField(max_length=20, help_text = 'Enter the place name',null=True)
    location = PointField(null=True, blank=True)
    description = models.TextField(max_length=2000,null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=15, null=True)
    type_of_place = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('place-detail', args=[str(self.id)])
