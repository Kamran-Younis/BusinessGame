from django.db import models
#Primery key ID automatically created in django for every model

#Represents a product
class Product(models.Model):

    #May replace product with an enumerated value to give a set list of products
    product = models.CharField(max_length=128, unique=True)
    baseCost = models.DecimalField(max_digits=9 , decimal_places=2)

    def __str__(self):
        return self.product

#represents a location
class Location(models.Model):
    locationName = models.CharField(max_length=128)
    #position on the map
    xPosition = models.IntegerField()
    yPosition = models.IntegerField()
    #the size value represents the population of people who can buy a product in a location
    size = models.IntegerField()

    def __str__(self):
        return self.locationName

#Represents a game. Could be player-owned or ai-Owned. ownership stated in User owns game
class Game(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


#Represents a business in a game. Could be player-owned or ai-Owned. ownership stated in User owns game
class Business(models.Model):
    businessName = models.CharField(max_length=128)
    CEOName = models.CharField(max_length=128)
    startingLocation = models.ForeignKey(Location, on_delete=models.CASCADE)
    productName = models.CharField(max_length=128)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) User table not defined yet

    def __str__(self):
        return self.businessName