from django.urls import path
from myapp2 import views
from .views import client_orders, orders, product_form, upload_image

urlpatterns = [
    path('', views.about, name='about'),
    path('client_order/<int:client_id>/<int:date_filter>', client_orders, name='client_orders'),
    path('order/<int:order_id>/', orders, name='orders'),
    path('product/manage/', product_form, name='product_form'),
    path('image/', upload_image, name='image_form'),
]