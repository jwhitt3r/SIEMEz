from django.contrib import admin
from .models import Event
from cases.models import Case
# Register your models here.


admin.site.register(Event)
admin.site.register(Case)