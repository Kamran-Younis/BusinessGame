from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    
    context_dict = {'boldmessage': 'This is a placeholder file'}
    
    return render(request, 'business_app/index.html', context=context_dict)

