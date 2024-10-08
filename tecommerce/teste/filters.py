from django_filters import rest_framework as filters
from teste.models import Client, Product, Employee, Sale

# Search Filters
LIKE = 'unaccent__icontains'
EQUALS = 'exact'
STARTS_WITH = 'startswith'


class ClientViewSet(filters.FilterSet):
    name = filters.CharFilter(lookup_expr=LIKE)
    cpf = filters.CharFilter(lookup_expr=STARTS_WITH)
    rg = filters.CharFilter(lookup_expr=STARTS_WITH)
    age = filters.NumberFilter(lookup_expr=EQUALS)
    class Meta:
        model = Client
        fields = ['name', 'cpf', 'rg', 'age']

class ProductViewSet(filters.FilterSet):

    class Meta:
        model = Product


class EmployeeViewSet(filters.FilterSet):
    class Meta:
        model = Employee


class SaleViewSet(filters.FilterSet):
    class Meta:
        model = Sale
