from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.models import User
from django.shortcuts import reverse



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    amount=models.IntegerField(default=0)
    total_amount=models.IntegerField(default=0)
    
    def total_cost(self):
        return self.quantity*self.product.price 
    

