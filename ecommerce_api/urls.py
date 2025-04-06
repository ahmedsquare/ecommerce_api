from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the E-commerce API!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
    path('api/auth/', include('users.urls')),
    path('', home, name='home'),  # Add this line to handle the root path
]
