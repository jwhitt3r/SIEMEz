from django.urls import path
from .views import EventList, EventDetail


urlpatterns = [
    path('<int:pk>/', EventDetail.as_view()),
    path('', EventList.as_view(), name="api"),
]