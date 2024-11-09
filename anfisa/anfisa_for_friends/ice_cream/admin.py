from django.contrib import admin

from .models import Category, IceCream, Topping, Wrapper

admin.site.register(Topping)
admin.site.register(Wrapper)
admin.site.register(IceCream)
admin.site.register(Category)