# orders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),  # URL for listing orders
    path('create/', views.order_create, name='order_create'),  # URL for creating a new order
    path('<int:pk>/', views.order_detail, name='order_detail'),  # URL for viewing a specific order
]
