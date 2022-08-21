from django.urls import path
from . import views

urlpatterns = [

    path('', views.Agronomist, name='Agronomist')
]