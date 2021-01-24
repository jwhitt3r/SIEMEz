from django.db import models
from django.contrib.auth import get_user_model
from siem.models import Event
from django.urls import reverse

class Case(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    case_name = models.CharField(max_length=60)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    connect_events = models.ManyToManyField(Event)
    case_notes = models.TextField()

    def __str__(self):
        return '{}'.format(self.case_name)

    def get_absolute_url(self):    
        return reverse('case_detail', args=[str(self.id)])