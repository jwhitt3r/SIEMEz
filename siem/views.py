from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.authtoken.models import Token
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
    ordering = ['-receivedat']

    # The following routine gathers all the events
    # and sorts them based on the search criteria
    # outputting into a queried result, which is
    # then displayed onto the template.
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
        query_filter = Q()  # initialize

        for get_param, kw_arg in attributes:
            get_value = self.request.GET.get(get_param)
            if get_value:
                query_filter |= Q(**{kw_arg: get_value})

        if self.start != '' and self.end == '':
            query_result = Event.objects.filter(
                query_filter, receivedat__gte=self.start).order_by('-receivedat')
        elif self.start == '' and self.end != '':
            query_result = Event.objects.filter(
                query_filter, receivedat__lt=self.end).order_by('-receivedat')
        elif self.start != '' and self.end != '':
            query_result = Event.objects.filter(query_filter, receivedat__range=(
                self.start, self.end)).order_by('-receivedat')
        elif self.start == '' and self.end == '':
            query_result = Event.objects.filter(
                query_filter).order_by('-receivedat')

        return query_result


class CreateApiTokenList(LoginRequiredMixin, TemplateView):
    context_object_name = 'user_list'
    login_url = 'account_login'
    template_name = 'siem/api_token.html'

    def get_context_data(self, **kwargs):
        context = super(CreateApiTokenList, self).get_context_data(**kwargs)
        context['user_token'] = Token.objects.get_or_create(
            user=self.request.user)
        return context


class EventDashboardView(LoginRequiredMixin, TemplateView):
    login_url = 'account_login'
    template_name = 'siem/event_dashboard.html'
    context_object_name = 'event_list'

    def get_context_data(self, **kwargs):
        context = super(EventDashboardView, self).get_context_data(**kwargs)

        # The following routine gathers all host ip objects.
        # If the host ip has a value it is then counted and added to the context object.
        # The value is then appended to the list ip_data and then set to the context object.

        self.ip_list = Event.objects.values_list(
            'fromhostip', flat=True).distinct()
        context['ip_labels'] = self.ip_list
        self.ip_data = []
        for self.ip in self.ip_list:
            self.ip_data.append(Event.objects.filter(
                fromhostip=self.ip).count())
        context['ip_data'] = self.ip_data

        # The following routine gathers all syslogtag objects,
        # splits the objects to remove the rsyslog processid e.g., CRON[1000].
        # This is then converted to a set to remove duplicates within our list.
        # This list is then looped to find the total amount of values via count.
        # If the label has a value that is greater than zero, the tag and data is added to the context object.

        self.syslogtag_split_list = []
        self.syslogtag_data = []
        self.syslogtag_list_with_value = []
        self.syslogtag_list = Event.objects.values_list(
            'syslogtag', flat=True).distinct()
        for item in self.syslogtag_list:
            self.syslogtag_split_list.append(item.split("[", 1)[0])

        for self.syslogtag in set(self.syslogtag_split_list):
            value = Event.objects.filter(syslogtag=self.syslogtag).count()
            if value > 0:
                self.syslogtag_list_with_value.append(self.syslogtag)
                self.syslogtag_data.append(Event.objects.filter(
                    syslogtag=self.syslogtag).count())
        context['syslogtag_data'] = self.syslogtag_data
        context['syslogtag_labels'] = self.syslogtag_list_with_value

        # The following routine gathers all facility objects and order by ascending value (0-10-n),
        # This list is then looped to find the total amount of values via count.
        # The value is then appended to the list facility_data and then set to the context object.

        self.facility_list = Event.objects.values_list(
            'facility', flat=True).distinct().order_by('facility')
        context['facility_labels'] = self.facility_list
        self.facility_data = []
        for self.facility in self.facility_list:
            self.facility_data.append(
                Event.objects.filter(facility=self.facility).count())
        context['facility_data'] = self.facility_data

        # The following routine gathers all priority objects order by ascending value (0-10-n),,
        # This list is then looped to find the total amount of values via count.
        # The value is then appended to the list priority_data and then set to the context object.

        self.priority_list = Event.objects.values_list(
            'priority', flat=True).distinct().order_by('priority')
        context['priority_labels'] = self.priority_list
        self.priority_data = []
        for self.priority in self.priority_list:
            self.priority_data.append(
                Event.objects.filter(priority=self.priority).count())
        context['priority_data'] = self.priority_data

        # The following routine gathers all fromhost objects.
        # This list is then looped to find the total amount of values via count.
        # The value is then appended to the list fromhost_data and then set to the context object.

        self.fromhost_list = Event.objects.values_list(
            'fromhost', flat=True).distinct()
        context['fromhost_labels'] = self.fromhost_list
        self.fromhost_data = []
        for self.fromhost in self.fromhost_list:
            self.fromhost_data.append(
                Event.objects.filter(fromhost=self.fromhost).count())
        context['fromhost_data'] = self.fromhost_data

        return context
