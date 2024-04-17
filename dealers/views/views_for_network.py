from rest_framework import generics

from dealers.models import RetailNetwork, Countries
from dealers.serializers import NetworkSerializer


class NetworkCreateAPIView(generics.CreateAPIView):
    """View for create Network"""
    queryset = RetailNetwork.objects.all()
    serializer_class = NetworkSerializer


class NetworkRetrieveAPIView(generics.RetrieveAPIView):
    """View for specific Network"""
    queryset = RetailNetwork.objects.all()
    serializer_class = NetworkSerializer


class NetworkUpdateAPIView(generics.UpdateAPIView):
    """View for update Network"""
    queryset = RetailNetwork.objects.all()
    serializer_class = NetworkSerializer


class NetworkListAPIView(generics.ListAPIView):
    """View for list Network. Can be filtered by country"""
    serializer_class = NetworkSerializer

    def get_queryset(self):
        queryset = RetailNetwork.objects.all()
        input_country = self.request.query_params.get('country')
        if input_country:
            country = Countries.objects.filter(title=input_country).first()
            queryset = queryset.filter(contacts__country=country)
        return queryset


class NetworkDeleteAPIView(generics.DestroyAPIView):
    """View for delete Network"""
    queryset = RetailNetwork.objects.all()
    serializer_class = NetworkSerializer

