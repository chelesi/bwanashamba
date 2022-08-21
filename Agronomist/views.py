from django.shortcuts import render
from .models import Agronomist

# Create your views here.

def Agronomist(request):
    #Agroengineer = agroengineer.objects.all('agroengineer')
    #agroengineer =  Agroengineer.objects.all()

      
    #context = {
        #'agroengineer': agroengineer
   # }

    return render(request, 'Agronomist/Agronomist.html') #, context

