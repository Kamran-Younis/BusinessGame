from django.shortcuts import render
from django.http import HttpResponse
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
    
    players = Player.objects.filter(game_end__lte=timezone.now()).order_by("game_end")
    business = Business.objects.filter(game_end__lte=timezone.now()).order_by("game_end")
    product = Product.objects.filter(game_end__lte=timezone.now()).order_by("game_end")
    
    if request.method == "POST":
        form1 = PlayerForm(request.POST)
        form2 = BusinessForm(request.POST)
        form3 = PlayerForm(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            player = form.save()
            business = form.save()
            product = form.save()
            business.save()
            player.save()
            product.save()
    else:
        form1 = PlayerForm()
        form2 = BusinessForm()
        form3 = ProductForm()

    return render(request, 'business_app/business_creation_page.html', {'form1':form1, 'form2':form2, 'form3':form3, 'players':players, 'business':business, 'product':product})