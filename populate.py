import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','business_app.settings')

import django
django.setup()
from business_game.models import Product,Location

def populate():
    products = [
        {'product': 'Phone',
         'baseCost': 100.00},
        {'product': 'Toy',
         'baseCost': 10.50},
        {'product': 'Food Item',
         'baseCost': 5.00}]

    locations = [
        {'locationName': 'London',
         'xPosition': 50,
         'yPosition': -50,
         'size': 9000000},
        {'locationName': 'Glasgow',
         'xPosition': 50,
         'yPosition': 25,
         'size': 600000}]

    for p in products:
        add_product(p["product"],p["baseCost"])

    for l in locations:
        add_location(l["locationName"],l["xPosition"],l["yPosition"],l["size"])

def add_product(product,baseCost):
    p = Product.objects.get_or_create(product=product, baseCost=baseCost)[0]
    p.save()
    return p

def add_location(locationName, xPosition, yPosition, size):
    l = Location.objects.get_or_create(locationName=locationName, xPosition=xPosition, yPosition=yPosition, size=size)[0]
    l.save()
    return l

if __name__ == '__main__':
    print('Starting population script...')
    populate()
    print('script complete')