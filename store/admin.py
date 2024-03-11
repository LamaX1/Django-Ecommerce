from django.contrib import admin
from .models import Category, Item, Order
from phone.models import Phone
from computer.models import Pcs

# Register your models here.
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Phone)
admin.site.register(Pcs)