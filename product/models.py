from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
class Item(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.TextField()
    price = models.IntegerField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')  


    def __str__(self) -> str:
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart') 

class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='orders')
    quantity= models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='orders')





