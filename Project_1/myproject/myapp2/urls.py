from django.urls import path
from myapp2 import views
from .views import client_orders, orders

urlpatterns = [
    path('', views.about, name='about'),
    path('client_order/<int:client_id>/<int:date_filter>', client_orders, name='client_orders'),
    path('order/<int:order_id>/', orders, name='orders')
]