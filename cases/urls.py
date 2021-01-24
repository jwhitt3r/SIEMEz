from django.urls import path
from .views import CaseListView, CaseDeleteView, CaseDetailView, CaseUpdateView, CaseCreateView
urlpatterns = [
    path('', CaseListView.as_view(), name='case_list'),
    path('<int:pk>/edit/', CaseUpdateView.as_view(), name='case_edit'),
    path('new/', CaseCreateView.as_view(), name='case_new'),
    path('<int:pk>/delete/', CaseDeleteView.as_view(), name='case_delete'),
    path('<int:pk>/', CaseDetailView.as_view(), name='case_detail'),
]