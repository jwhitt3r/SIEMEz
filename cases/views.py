from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Case
from siem.models import Event
from .forms import CustomCaseUpdate, CustomCaseNew


class CaseListView(LoginRequiredMixin, ListView):
    model = Case
    template_name = 'cases/case_list.html'
    context_object_name = 'case_list'
    login_url = 'account_login'
    ordering = ['-date_created']

class CaseDetailView(LoginRequiredMixin, DetailView):
    model = Case
    context_object_name = 'case_list'
    template_name = 'cases/case_detail.html'

class CaseUpdateView(LoginRequiredMixin, UpdateView):
    model = Case
    template_name = 'cases/case_edit.html'
    form_class = CustomCaseUpdate


class CaseDeleteView(LoginRequiredMixin, DeleteView):
    model = Case
    template_name = 'cases/case_delete.html'
    success_url = reverse_lazy('case_list')
    
class CaseCreateView(LoginRequiredMixin, CreateView):
    model = Case
    template_name = 'cases/case_new.html'
    form_class = CustomCaseNew