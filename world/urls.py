from django.urls import path
from . import views
from .views import EntryList, ListaColectivos

urlpatterns= [
	path('', views.home, name='home'),
	path('puntos', EntryList.as_view(), name='puntos'),
	path('listacolectivos/', ListaColectivos.as_view(), name='lista'),
]