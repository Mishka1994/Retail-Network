from rest_framework import generics
from dealers.models import Contacts
from dealers.serializers import ContactsSerializer


class ContactCreateAPIView(generics.CreateAPIView):
    """View for create Contacts"""
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class ContactListAPIView(generics.ListAPIView):
    """View for get list all contacts"""
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class ContactDeleteAPIView(generics.DestroyAPIView):
    """View for delete Contacts"""
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


