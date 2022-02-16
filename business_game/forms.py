from django import forms
from .models import Player, Business, Product

PRODUCT_CHOICES = [('Toy','toy'),('Phone','phone'),('Car','car'),('Robot','robot'),('Food','food')]
LOCATIONS = [('Edinburgh','edinburgh'),('London','london'),('Belfast','belfast'),('Cardiff','cardiff')]

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('name',)
        
class BusinessForm(forms.ModelForm):

    starting_location = forms.CharField(label = 'Starting Loaction', widget = forms.Select(choices=LOCATIONS))

    class Meta:
        model = Business
        fields = ('business_name','product_name','starting_location')
        
class ProductForm(forms.ModelForm):

    product = forms.CharField(label = 'Product Type', widget = forms.Select(choices=PRODUCT_CHOICES))
    
    class Meta:
        model = Product
        fields = ('product',)
        