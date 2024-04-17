from django.contrib import admin
from dealers.models import Factory, RetailNetwork, IndividualEntrepreneur


@admin.action(description='Очистить задолженность')
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'contacts', 'provider', 'time_to_create', 'debt', 'link_to_provider',)
    list_filter = ('contacts__city', )
    search_fields = ('title', )
    actions = [clear_debt]

    def link_to_provider(self, obj):
        if obj.provider_id is None:
            return 'Поставщик не указан'
        else:
            return f'http://localhost:8000/factory/retrieve/{obj.provider_id}'


@admin.register(RetailNetwork)
class RetailNetworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'contacts', 'provider', 'time_to_create', 'debt', 'link_to_provider', )
    list_filter = ('contacts__city', )
    search_fields = ('title', )
    actions = [clear_debt]

    def link_to_provider(self, obj):
        if obj.provider_id is None:
            return 'Поставщик не указан'
        else:
            return f'http://localhost:8000/factory/retrieve/{obj.provider_id}'


@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('title', 'contacts', 'provider', 'time_to_create', 'debt', 'link_to_provider',)
    list_filter = ('contacts__city', )
    search_fields = ('title', )
    actions = [clear_debt]

    def link_to_provider(self, obj):
        if obj.provider_id is None:
            return 'Поставщик не указан'
        else:
            return f'http://localhost:8000/network/retrieve/{obj.provider_id}'
