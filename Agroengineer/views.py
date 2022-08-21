from django.shortcuts import render
from .models import Agroengineer

# Create your views here.

def Agroengineer(request):
    #Agroengineer = agroengineer.objects.all('agroengineer')
    #agroengineer =  Agroengineer.objects.all()

      
    #context = {
        #'agroengineer': agroengineer
   # }

    return render(request, 'Agroengineer/Agroengineer.html') #, context

