from django.contrib import admin

from .models import Dish, Category, Additional

# Register your models here.
admin.site.register(Dish)
admin.site.register(Category)
admin.site.register(Additional)
