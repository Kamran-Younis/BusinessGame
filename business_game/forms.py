from django import forms
from .models import *


        
class BusinessForm(forms.ModelForm):
    businessName = forms.CharField(label = 'Name Your Business')
    CEOName = forms.CharField(label = 'Your Name')
    productName = forms.CharField(label = 'Name Your Product')

    startingLocation = forms.ModelChoiceField(label="Choose your starting location", queryset=Location.objects.all())

    class Meta:
        model = Business
        fields = ('businessName','CEOName','productName','startingLocation')

class GameForm(forms.ModelForm):
    product = forms.ModelChoiceField(label="Choose your product type", queryset=Product.objects.all())

    class Meta:
        model = Game
        fields = ('product',)