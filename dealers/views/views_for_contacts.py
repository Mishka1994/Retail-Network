from rest_framework import generics

from dealers.models import Contacts
from dealers.serializers import ContactsSerializer


class ContactCreateAPIView(generics.CreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class ContactDeleteAPIView(generics.DestroyAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


