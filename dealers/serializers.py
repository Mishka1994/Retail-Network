from rest_framework import serializers

from dealers.models import Countries, Contacts, Products, Factory


class CountriesSerializer(serializers.ModelSerializer):

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


class FactorySerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        if validated_data.get('debt'):
            raise serializers.ValidationError('Нельзя изменять поле debt')

        instance.title = validated_data.get('title', instance.title)
        instance.contacts = validated_data.get('contacts', instance.contacts)
        if validated_data.get('products'):
            input_products = validated_data.get('products')
            instance.products.set(input_products)
        instance.provider = validated_data.get('provider', instance.provider)

        return instance

    class Meta:
        model = Factory
        fields = '__all__'

