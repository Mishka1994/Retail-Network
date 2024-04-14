from django.urls import path

from dealers.apps import DealersConfig
from dealers.views.views_for_contacts import ContactCreateAPIView, ContactDeleteAPIView
from dealers.views.views_for_country import CountryCreateAPIView, CountryDeleteAPIView
from dealers.views.views_for_product import ProductCreateAPIView, ProductDeleteAPIView

app_name = DealersConfig.name


urlpatterns = [
    # Country-urls
    path('countries/create/', CountryCreateAPIView.as_view(), name='country-create'),
    path('countries/delete/<int:pk>/', CountryDeleteAPIView.as_view(), name='country-delete'),

    # Contacts-urls
    path('contacts/create/', ContactCreateAPIView.as_view(), name='contacts-create'),
    path('contacts/delete/<int:pk>/', ContactDeleteAPIView.as_view(), name='contacts-delete'),

    # Products-urls
    path('products/create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('products/delete/<int:pk>/', ProductDeleteAPIView.as_view(), name='product-delete'),

]
