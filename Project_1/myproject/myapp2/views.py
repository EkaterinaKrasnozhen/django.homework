from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404, render
from myapp2.models import Order
from myapp2.models import Client
from datetime import datetime, timedelta
from .forms import ProductForm, ImageForm
from .models import Product



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


def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            prod_id = form.cleaned_data['prod_id']
            name = form.cleaned_data['name']
            title = form.cleaned_data['title']
            price = form.cleaned_data['price']
            count = form.cleaned_data['count']
            product = Product.objects.filter(pk=prod_id).first()
            product.name = name
            product.title = title
            product.price = price
            product.count = count
            #product.image = image
            product.save()
    else:
        form = ProductForm()
    return render(request, 'myapp2/product_form.html', {'form': form})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'myapp2/upload_image.html', {'form': form})