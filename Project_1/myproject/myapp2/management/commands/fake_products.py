from django.core.management.base import BaseCommand
from myapp2.models import Product


class Command(BaseCommand):
    help = "Create fake products."
    
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Product ID')
    
    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            product = Product(name=f'product{i}', title=f'very good product', price=1342.5 + i, count=i + 10)
            product.save()