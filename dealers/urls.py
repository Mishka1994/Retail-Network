from django.urls import path

from dealers.apps import DealersConfig
from dealers.views.views_for_contacts import ContactCreateAPIView, ContactDeleteAPIView, ContactListAPIView
from dealers.views.views_for_country import CountryCreateAPIView, CountryDeleteAPIView
from dealers.views.views_for_factory import FactoryCreateAPIView, FactoryRetrieveAPIView, FactoryUpdateAPIView, \
    FactoryListAPIView, FactoryDeleteAPIView
from dealers.views.views_for_network import NetworkCreateAPIView, NetworkRetrieveAPIView, NetworkUpdateAPIView, \
    NetworkListAPIView, NetworkDeleteAPIView
from dealers.views.views_for_product import ProductCreateAPIView, ProductDeleteAPIView, ProductListAPIView

app_name = DealersConfig.name


urlpatterns = [
    # Country-urls
    path('countries/create/', CountryCreateAPIView.as_view(), name='country-create'),
    path('countries/delete/<int:pk>/', CountryDeleteAPIView.as_view(), name='country-delete'),

    # Contacts-urls
    path('contacts/create/', ContactCreateAPIView.as_view(), name='contacts-create'),
    path('contacts/list/', ContactListAPIView.as_view(), name='contacts-list'),
    path('contacts/delete/<int:pk>/', ContactDeleteAPIView.as_view(), name='contacts-delete'),

    # Products-urls
    path('products/create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('products/list/', ProductListAPIView.as_view(), name='product-list'),
    path('products/delete/<int:pk>/', ProductDeleteAPIView.as_view(), name='product-delete'),

    # Factory-urls
    path('factory/create/', FactoryCreateAPIView.as_view(), name='factory-create'),
    path('factory/retrieve/<int:pk>/', FactoryRetrieveAPIView.as_view(), name='factory-retrieve'),
    path('factory/update/<int:pk>/', FactoryUpdateAPIView.as_view(), name='factory-update'),
    path('factory/list/', FactoryListAPIView.as_view(), name='factory-list'),
    path('factory/delete/<int:pk>/', FactoryDeleteAPIView.as_view(), name='factory-delete'),

    # Network-urls
    path('network/create/', NetworkCreateAPIView.as_view(), name='network-create'),
    path('network/retrieve/<int:pk/', NetworkRetrieveAPIView.as_view(), name='network-retrieve'),
    path('network/update/<int:pk>/', NetworkUpdateAPIView.as_view(), name='network-update'),
    path('network/list/', NetworkListAPIView.as_view(), name='network-list'),
    path('network/delete/<int:pk>/', NetworkDeleteAPIView.as_view(), name='network-delete'),


]
