from django.urls import path,include
from . import views

urlpatterns = [

    path('', views.Agroengineer, name='Agroengineer'),
    #path('', include('django.contrib.auth.urls'))
]