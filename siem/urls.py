from django.urls import path
from .views import HomePageView, EventListView, SearchEventResultsListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('event/', EventListView.as_view(), name='event'),
    path('search_event/', SearchEventResultsListView.as_view(), name='search_event'),
]
