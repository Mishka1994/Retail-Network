from rest_framework import generics

from dealers.models import Products
from dealers.serializers import ProductsSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
