from django.core.management.base import BaseCommand
from myapp2.models import Client, Order, Product


class Command(BaseCommand):
    help = "Create fake orders."
    
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Order ID')
    
    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        clients = Client.objects.filter(pk=count)        
        for client in clients:
            order = Order(client=client, amount=0)
            order.save()
        products = Product.objects.all().order_by('pk')[:count]
        for product in products:
            order.product.add(product)
            order.amount += product.price
            order.save()
        
            
        
            
                