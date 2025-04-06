# products/views.py

from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter
from rest_framework.pagination import PageNumberPagination

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

class ProductPagination(PageNumberPagination):
    page_size = 10  # Define number of items per page
    page_size_query_param = 'page_size'
    max_page_size = 100