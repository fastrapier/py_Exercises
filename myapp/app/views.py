from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from app.models import Product, Order


def register_page(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'register.html', context)


def orders_page(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, "orders.html", context)


def homepage(request):
    context = {'products': Product.objects.all()}
    return render(request, "Home.html", context)
