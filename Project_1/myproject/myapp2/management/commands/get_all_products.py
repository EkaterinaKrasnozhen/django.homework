from django.core.management.base import BaseCommand
from myapp2.models import Product


class Command(BaseCommand):
    help = "Get all products."
    
    def handle(self, *args, **kwargs):
        prod = Product.objects.all()
        self.stdout.write(f'{prod}')