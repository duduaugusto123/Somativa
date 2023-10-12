import django_filters
from django_filters import *
from .models import CustomUser


class CustomUserFilter(django_filters.FilterSet):
    # Filtros personalizados (exemplos)
    username = CharFilter(field_name='user__username', lookup_expr='icontains')
    data_nasc_min = NumberFilter(field_name='data_nasc', lookup_expr='gte')
    data_nasc_max = NumberFilter(field_name='data_nasc', lookup_expr='lte')

    class Meta:
        model = CustomUser
        fields = ['type', 'cpf']