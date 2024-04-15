from rest_framework import generics

from dealers.models import Factory
from dealers.serializers import FactorySerializer


class FactoryCreateAPIView(generics.CreateAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class FactoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class FactoryUpdateAPIView(generics.UpdateAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class FactoryListAPIView(generics.ListAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class FactoryDeleteAPIView(generics.DestroyAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


