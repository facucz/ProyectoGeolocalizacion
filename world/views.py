from django.shortcuts import render
from django.urls import path
from django.views.generic import ListView
from .models import Entry


class EntryList(ListView):
    queryset = Entry.objects.filter(point__isnull=False)


def home(request):
    return render(request, 'home.html', {})
