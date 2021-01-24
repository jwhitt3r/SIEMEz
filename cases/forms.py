from django import forms
from .models import Case
from siem.models import Event
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.db.models import Count

class CustomCaseUpdate(forms.ModelForm):
    connect_events = forms.ModelMultipleChoiceField( queryset=Event.objects.all().order_by('-receivedat'), widget=forms.widgets.CheckboxSelectMultiple())
    class Meta:
        model = Case
        fields = ('case_name','author','case_notes', 'connect_events',)
        labels = {
            'connect_events': 'Connected Events',
            'case_name': 'Case Name',
            'author': 'Author',
            'case_notes': 'Case Notes',
        }

class CustomCaseNew(forms.ModelForm):
    connect_events = forms.ModelMultipleChoiceField( queryset=Event.objects.all().order_by('-receivedat'), widget=forms.widgets.CheckboxSelectMultiple())
    class Meta:
        model = Case
        fields = ('case_name', 'author', 'case_notes', 'connect_events',  )

        labels = {
            'connect_events': 'Connected Events',
            'case_name': 'Case Name',
            'author': 'Author',
            'case_notes': 'Case Notes',
        }
    