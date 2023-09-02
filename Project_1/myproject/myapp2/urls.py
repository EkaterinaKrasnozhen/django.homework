from django.urls import path
from myapp2 import views

urlpatterns = [
    path('', views.about, name='about'),
]