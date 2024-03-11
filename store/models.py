from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    item_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(default=0,decimal_places=2,max_digits=7, null=True)
    image = models.CharField(max_length=150, null=True)
    color = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.item_category.name
    
class Order(models.Model):
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=50,null=True)
    customer = models.IntegerField()
    quantity= models.IntegerField(default=1)
    price = models.DecimalField(default=0,decimal_places=2,max_digits=7, null=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.item_name

