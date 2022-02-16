from django.db import models
from django.utils import timezone



#Represents a product
class Product(models.Model):

    #May replace product with an enumerated value to give a set list of products
    product = models.CharField(max_length=128, null = False)
    baseCost = models.DecimalField(max_digits=9 , decimal_places=2, null = False)
    game_end = models.DateTimeField(blank=True, null=True)
    
    def gameover(self):
        self.game_end = timezone.now()
        self.save()

    def __str__(self):
        return self.product

class Business(models.Model):
    business_name = models.CharField(max_length=128, null = False)
    starting_location = models.CharField(max_length=128, null = False)
    product_name = models.CharField(max_length=128, null = False)
    game_end = models.DateTimeField(blank=True, null=True)
    #game = models.ForeignKey(Game, on_delete=models.CASCADE) Game table not yet defined
    
    def gameover(self):
        self.game_end = timezone.now()
        self.save()

    def __str__(self):
        return self.businessName
        
class Player(models.Model):
    name = models.CharField(max_length=200)
    score = models.IntegerField(
            blank=True, null=True)
    game_end = models.DateTimeField(
            blank=True, null=True)

    def gameover(self):
        self.game_end = timezone.now()
        self.save()

    def __str__(self):
        return self.name