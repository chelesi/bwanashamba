from django.shortcuts import render

# Create your views here.
def customer(request):
    
    customer = customer.objects.all()
    
    context = {
        'customer': customer
    }

    return render(request, 'customer/ customer.html', context)
