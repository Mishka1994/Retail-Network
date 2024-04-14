from rest_framework import serializers

from dealers.models import Countries, Contacts, Products


class CountrysSerializer(serializers.ModelSerializer):

    class Meta:
        model = Countries
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacts
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'
