from django.db import models

#Represents a product
class Product(models.Model):

    #May replace product with an enumerated value to give a set list of products
    product = models.CharField(max_length=128, unique=True, null = False)
    baseCost = models.DecimalField(max_digits=9 , decimal_places=2, null = False)

    def __str__(self):
        return self.product

class Business(models.Model):
    businessName = models.CharField(max_length=128, null = False)
    startingLocation = models.CharField(max_length=128, null = False)
    productName = models.CharField(max_length=128, null = False)
    #game = models.ForeignKey(Game, on_delete=models.CASCADE) Game table not yet defined

    def __str__(self):
        return self.businessName