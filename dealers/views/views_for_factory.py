from rest_framework import generics
from dealers.models import Factory, Countries
from dealers.permissions import IsActivate
from dealers.serializers import FactorySerializer


class FactoryCreateAPIView(generics.CreateAPIView):
    """View for create Factory"""
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    permission_classes = [IsActivate, ]


class FactoryRetrieveAPIView(generics.RetrieveAPIView):
    """View for specific Factory"""
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class FactoryUpdateAPIView(generics.UpdateAPIView):
    """View for update Factory"""
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class FactoryListAPIView(generics.ListAPIView):
    """View for list Factory. Can be filtered by country"""
    serializer_class = FactorySerializer

    def get_queryset(self):
        queryset = Factory.objects.all()
        input_country = self.request.query_params.get('country')
        if input_country:
            country = Countries.objects.filter(title=input_country).first()
            queryset = queryset.filter(contacts__country=country)
        return queryset


class FactoryDeleteAPIView(generics.DestroyAPIView):
    """View for delete Factory"""
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
