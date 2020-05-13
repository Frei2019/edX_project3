from django.urls import path

from . import views

from .models import Dish

urlpatterns = [
    path("", views.index, name="index"),
    path("/register", views.register, name="register"),
    path("/menu", views.menu, name="menu"),
    path("/login", views.login, name='login'),
]
