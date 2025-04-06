from rest_framework import viewsets, permissions
from .models import Product
from .serializers import ProductSerializer
from rest_framework import filters

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'category', 'artist_name', 'medium']
    ordering_fields = ['created_at', 'price']
