from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from dealers.models import Factory, Countries, Contacts
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
    # queryset = Factory.objects.all()
    serializer_class = FactorySerializer

    def get_queryset(self):
        queryset = Factory.objects.all()
        input_country = self.request.query_params.get('country')
        if input_country:
            country = Countries.objects.filter(title=input_country).first()
            # necessary_contacts = Contacts.objects.filter(country=country)
            queryset = queryset.filter(contacts__country=country)
        return queryset


class FactoryDeleteAPIView(generics.DestroyAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


