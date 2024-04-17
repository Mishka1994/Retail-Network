from rest_framework import generics
from dealers.models import Factory, Countries
from dealers.permissions import IsActivate
from dealers.serializers import FactorySerializer


class FactoryCreateAPIView(generics.CreateAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    permission_classes = [IsActivate, ]


class FactoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class FactoryUpdateAPIView(generics.UpdateAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class FactoryListAPIView(generics.ListAPIView):
    serializer_class = FactorySerializer

    def get_queryset(self):
        queryset = Factory.objects.all()
        input_country = self.request.query_params.get('country')
        if input_country:
            country = Countries.objects.filter(title=input_country).first()
            queryset = queryset.filter(contacts__country=country)
        return queryset


class FactoryDeleteAPIView(generics.DestroyAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
