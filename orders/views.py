from django.http import HttpResponse
from django.shortcuts import render

from .models import Dish, Category

# Create your views here.
def index(request):
    context = {}
    if not request.user.is_authenticated:
        context["logged_in"] = 0
    else:
        context["logged_in"] = 1
    return render(request, "orders/index.html", context)

def login(request):
    context = {}
    return render(request, "orders/login.html", context)

def register(request):
    context = {}
    # TODO: change to the register page
    return render(request, "orders/index.html", context)

def menu(request):
    context = {
        "dishes": Dish.objects.all(),
        "categories": Category.objects.all()
    }
    return render(request, "orders/menu.html", context)
