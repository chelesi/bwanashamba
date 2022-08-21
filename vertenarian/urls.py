from django.urls import path
from . import views

urlpatterns = [

    path('', views.vertenarian, name='vertenarian')
]