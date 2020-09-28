from django.urls import path
from . import views
from .views import EntryList

urlpatterns= [
	path('', views.home, name='home'),
	path('puntos', EntryList.as_view(), name='puntos'),	
]