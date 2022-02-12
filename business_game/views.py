from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    
    context_dict = {}
    
    return render(request, 'business_app/index.html', context=context_dict)


def business_page(request):
    context_dict = {}

    return render(request, 'business_app/business_page.html', context=context_dict)

