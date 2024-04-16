from rest_framework import generics

from dealers.models import IndividualEntrepreneur
from dealers.serializers import EntrepreneurSerializer


class EntrepreneurCreateAPIView(generics.CreateAPIView):
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer


class EntrepreneurRetrieveAPIView(generics.RetrieveAPIView):
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer


class EntrepreneurUpdateAPIView(generics.UpdateAPIView):
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer


class EntrepreneurListAPIView(generics.ListAPIView):
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer


class EntrepreneurDeleteAPIView(generics.DestroyAPIView):
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer

