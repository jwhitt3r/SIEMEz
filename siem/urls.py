from django.urls import path
from .views import HomePageView, EventListView, SearchEventResultsListView, CreateApiTokenList, EventDashboardView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('event/', EventListView.as_view(), name='event'),
    path('search_event/', SearchEventResultsListView.as_view(), name='search_event'),
    path('api_token/', CreateApiTokenList.as_view(), name='api_token'),
    path('event_dashboard/', EventDashboardView.as_view(), name='event_dashboard'),
]
