from django.shortcuts import render
from .models import Vertenarian

# Create your views here.

def vertenarian(request):
    # Get all realtors
    Customer = Vertenarian.objects.all()     #order_by('-hire_date')

    # Get MVP
    #mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        ' Customer ':  vertenarian,
        #'mvp_realtors': mvp_realtors
    }

    return render(request, 'vertenarian/vertenarian.html', context)


#def vertenarian(request):
  #  Vertenarian = vertenarian.objects.all()
     
   # context = {
    #    'Vertenarian': Vertenarian
    #}

   
    #return render(request, 'vertenarian/vertenarian.html', context)
