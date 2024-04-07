import datetime
from django.shortcuts import get_object_or_404, render
from .models import Client, Product, Order

# Create your views here.
def client_orders_week(request, client_id):
    date = datetime.datetime.now()
    new_date = date - datetime.timedelta(days = 7)
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(customer=client, date_ordered__gte=new_date).order_by('-date_ordered')
    s = set()
    for order in orders:
        products = Product.objects.filter(order=order)
        for product in products:
            s.add(product)
    return render(request, 'secondapp/sorted_orders.html', {'client': client, 'products': s})


def client_orders_month(request, client_id):
    date = datetime.datetime.now()
    new_date = date - datetime.timedelta(days = 31)    
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(customer=client, date_ordered__gte=new_date).order_by('-date_ordered')
    s = set()
    for order in orders:
        products = Product.objects.filter(order=order)
        for product in products:
            s.add(product)
    return render(request, 'secondapp/sorted_orders.html', {'client': client, 'products': s})


def client_orders_year(request, client_id):
    date = datetime.datetime.now()
    new_date = date - datetime.timedelta(days = 365)     
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(customer=client, date_ordered__gte=new_date).order_by('-date_ordered')
    s = set()
    for order in orders:
        products = Product.objects.filter(order=order)
        for product in products:
            s.add(product)
    return render(request, 'secondapp/sorted_orders.html', {'client': client, 'products': s})   