from django.core.management.base import BaseCommand
from myapp2.models import Order


class Command(BaseCommand):
    help = "Get order by id."
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')
    
    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        amount=0
        order = Order.objects.filter(pk=pk).first()
        products_in_order = order.product.all()
        for product in products_in_order:
            amount += product.price
        return f'{amount}'
        