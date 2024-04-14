from rest_framework import generics

from dealers.models import Countries
from dealers.serializers import CountrysSerializer


class CountryCreateAPIView(generics.CreateAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountrysSerializer


class CountryDeleteAPIView(generics.DestroyAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountrysSerializer
