from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, state_choices 

from listings.models import Listing
from customer.models import customer

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    Customer =customer.objects.all()  #order_by('-hire_date')

    # Get MVP
    #mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        ' Customer ':  Customer ,
        #'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)

    

#Here i have to add a listing page which will be redircted from a  pages view our featured lings