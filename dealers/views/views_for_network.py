from rest_framework import generics

from dealers.models import RetailNetwork
from dealers.serializers import NetworkSerializer


class NetworkCreateAPIView(generics.CreateAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = NetworkSerializer


class NetworkRetrieveAPIView(generics.RetrieveAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = NetworkSerializer


class NetworkUpdateAPIView(generics.UpdateAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = NetworkSerializer


class NetworkListAPIView(generics.ListAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = NetworkSerializer


class NetworkDeleteAPIView(generics.DestroyAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = NetworkSerializer

