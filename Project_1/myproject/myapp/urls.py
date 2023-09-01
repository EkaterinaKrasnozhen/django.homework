from django.urls import path
from myapp import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('start/', views.start, name='start'),
]