from rest_framework import generics

from dealers.models import Products
from dealers.serializers import ProductsSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Products
    serializer_class = ProductsSerializer


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Products
    serializer_class = ProductsSerializer
