from rest_framework import generics

from dealers.models import IndividualEntrepreneur, Countries
from dealers.serializers import EntrepreneurSerializer


class EntrepreneurCreateAPIView(generics.CreateAPIView):
    """View for create Entrepreneur"""
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer


class EntrepreneurRetrieveAPIView(generics.RetrieveAPIView):
    """View for specific Entrepreneur"""
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer


class EntrepreneurUpdateAPIView(generics.UpdateAPIView):
    """View for update Entrepreneur"""
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer


class EntrepreneurListAPIView(generics.ListAPIView):
    """View for list Entrepreneur. Can be filtered by country"""
    serializer_class = EntrepreneurSerializer
    def get_queryset(self):
        queryset = IndividualEntrepreneur.objects.all()
        input_country = self.request.query_params.get('country')
        if input_country:
            country = Countries.objects.filter(title=input_country).first()
            queryset = queryset.filter(contacts__country=country)
        return queryset


class EntrepreneurDeleteAPIView(generics.DestroyAPIView):
    """View for delete Entrepreneur"""
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer

