from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from myapp2.models import Order
from myapp2.models import Client
from datetime import datetime, timedelta


def about(request):
    return HttpResponse('Hello')


def client_orders(request, client_id, date_filter):
    now = datetime.now()   
    filter_date = now - timedelta(days=date_filter)
    client = get_object_or_404(Client, pk=client_id)
    client_orders = Order.objects.filter(client=client).filter(date__gte=filter_date)
    return render(request, 'myapp2/clients_orders.html', {'client': client, 'orders': client_orders})


def orders(request, order_id):
    order = Order.objects.filter(pk=order_id).first()
    product_in_order = order.product.all()
    return render(request, 'myapp2/orders.html', {'order': order, 'products': product_in_order})