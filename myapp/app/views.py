from django.shortcuts import render

from app.models import Order, Product


def orders_page(request):
    return render(request, "orders.html")


def homepage(request):
    return render(request, "Home.html")
