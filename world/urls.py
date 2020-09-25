from django.urls import path
from . import views
from .views import EntryList

urlpatterns= [
	path('', EntryList.as_view()),
	
]