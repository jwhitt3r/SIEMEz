from django.shortcuts import render
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Event

class HomePageView(TemplateView):
    template_name = 'home.html'


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'siem/event.html'
    context_object_name = 'event_list'
    login_url = 'account_login'

class SearchEventResultsListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'siem/search_event.html'
    context_object_name = 'event_list'
    login_url = 'account_login'

    def get_queryset(self):
        hostname = self.request.GET.get('hostname')
        return Event.objects.filter(
            Q(fromhost__icontains=hostname)
        )
    


