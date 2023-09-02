from django.core.management.base import BaseCommand
from myapp2.models import Client, Order, Product


class Command(BaseCommand):
    help = "Create fake orders."
    
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Order ID')
    
    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        clients = Client.objects.filter(pk=count)
        # for i in range(1, count + 1):
        #     products = Product(name=f'product{i}', title=f'very good product', price=1342.5 + i, count=i + 10)
        #     products.save()
        
        for client in clients:
            order = Order(client=client, amount=664000)
            order.save()
        products = Product.objects.filter(pk=count)
        for product in products:
            order.product.add(product)
            order.save()
        
            
                