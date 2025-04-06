from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the E-commerce API!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('auth/', include('users.urls')),
    path('orders/', include('orders.urls')),  
    path('', home, name='home'), 
]
