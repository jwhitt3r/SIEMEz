from django.shortcuts import render
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from psycopg2.extras import DateTimeTZRange

from .models import Event

class HomePageView(TemplateView):
    template_name = 'home.html'


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'siem/event.html'
    context_object_name = 'event_list'
    login_url = 'account_login'
    paginate_by = 25
    ordering = ['-receivedat']

class SearchEventResultsListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'siem/search_event.html'
    context_object_name = 'event_list'
    login_url = 'account_login'
    paginate_by = 25
    def get_queryset(self):
        self.start = self.request.GET.get('start', '')
        self.end = self.request.GET.get('end', '')

        attributes = (
            ('hostname', 'fromhost__icontains'),
            ('facility', 'facility__icontains'),
            ('priority', 'priority__icontains'),
            ('syslogtag', 'syslogtag__icontains'),
            ('message', 'message__icontains'),
            ('ip', 'fromhostip__icontains'),
            )
        query_filter = Q() # initialize

        for get_param, kw_arg in attributes:
            get_value = self.request.GET.get(get_param)
            if get_value:
                query_filter |= Q(**{ kw_arg: get_value })

        if self.start != '' and self.end == '':
            query_result = Event.objects.filter(query_filter, receivedat__gte=self.start).order_by('-receivedat')
        if self.start == '' and self.end != '':
            query_result = Event.objects.filter(query_filter, receivedat__lt=self.end).order_by('-receivedat')
        if self.start != '' and self.end != '':
            query_result = Event.objects.filter(query_filter, receivedat__range=(self.start, self.end)).order_by('-receivedat')
        if self.start == '' and self.end == '':      
            query_result = Event.objects.filter(query_filter).order_by('-receivedat')

        
        return query_result
    


