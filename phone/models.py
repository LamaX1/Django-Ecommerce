from django.db import models
from store.models import Category, Item


# Create your models here.
class Phone(models.Model):
    phone_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.CharField(max_length=150)
    color = models.CharField(max_length=50)
    description = models.CharField(max_length=350, default='', blank=True, null=True)
    price = models.DecimalField(default=0,decimal_places=2,max_digits=7)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.phone_category.name
    