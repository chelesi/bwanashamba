from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
# Create your views here.

def kilimoView(request):
    return render(request , 'kilimo/kilimo.html')

      