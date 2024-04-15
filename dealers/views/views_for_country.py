from rest_framework import generics

from dealers.models import Countries
from dealers.serializers import CountriesSerializer


class CountryCreateAPIView(generics.CreateAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer


class CountryDeleteAPIView(generics.DestroyAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
