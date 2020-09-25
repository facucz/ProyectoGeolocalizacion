from django.urls import path
from django.views.generic import ListView
from .models import Entry


class EntryList(ListView):
    queryset = Entry.objects.filter(point__isnull=False)

# Create your views here.

