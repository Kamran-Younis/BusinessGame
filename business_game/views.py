from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import *
from .models import *
from django.utils import timezone


def index(request):
    
    context_dict = {}
    
    return render(request, 'business_app/index.html', context=context_dict)


def business_page(request):
    context_dict = {}

    return render(request, 'business_app/business_page.html', context=context_dict)

def business_creation_page(request):
    
    if request.method == "POST":
        business_form = BusinessForm(request.POST)
        game_form = GameForm(request.POST)
        if game_form.is_valid() and game_form.is_valid():
            business = business_form.save(commit=False)
            game = game_form.save()
            business.game = game
            business.save()
            game.save()
            return redirect("/business_app/business_page")
    else:
        business_form = BusinessForm()
        game_form = GameForm()

    return render(request, 'business_app/business_creation_page.html', {'business_form':business_form, 'game_form':game_form})
    
def location_page_london(request):
    context_dict = {}
    
    return render(request, 'business_app/location_page_london.html', context=context_dict)
    
def location_page_glasgow(request):
    context_dict = {}
    
    return render(request, 'business_app/location_page_glasgow.html', context=context_dict)