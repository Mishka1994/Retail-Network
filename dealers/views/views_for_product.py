from rest_framework import generics
from dealers.models import Products
from dealers.serializers import ProductsSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    """View for create Product"""
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductListAPIView(generics.ListAPIView):
    """View for list Product"""
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductDeleteAPIView(generics.DestroyAPIView):
    """View for delete Product"""
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
