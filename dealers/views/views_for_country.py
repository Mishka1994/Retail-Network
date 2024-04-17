from rest_framework import generics
from dealers.models import Countries
from dealers.serializers import CountriesSerializer


class CountryCreateAPIView(generics.CreateAPIView):
    """View for create Country"""
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer


class CountryListAPIView(generics.ListAPIView):
    """View for get list of Countries"""
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer


class CountryDeleteAPIView(generics.DestroyAPIView):
    """View for delete Country"""
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
