from django.shortcuts import render
from django.urls import path
from django.views.generic import ListView
from .models import Entry, LineaColectivo


class EntryList(ListView):
    queryset = Entry.objects.filter(point__isnull=False)


def home(request):
    return render(request, 'home.html', {})


class ListaColectivos(ListView):

    model = LineaColectivo
    template_name = "lista_colectivos.html"

    def get_queryset(self):
        lineasColectivos = LineaColectivo.objects.all()
        return lineasColectivos
