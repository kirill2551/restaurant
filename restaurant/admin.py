from django.contrib import admin
from .models import Dish
from .models import Dish, Category
from .models import CartItem
admin.site.register(Dish)
admin.site.register(Category)
admin.site.register(CartItem)
