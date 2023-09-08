from django.db import models
from django.db.models import F, Sum


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    regist = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Name: {self.name}, email: {self.email}, phone: {self.phone}, address: {self.address}'

    

class Product(models.Model):
    name = models.CharField(max_length=100)
    title = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    add_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name}, {self.price}, {self.get_title()}'
    
    def get_price(self):
        return self.price
    
    def get_title(self):
        words = self.title.split()
        return f'{" ".join(words[:2])}...'
    
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f'Order_id: {self.pk}, Client_id: {self.client.pk}, {self.product}'
    
        
    
        