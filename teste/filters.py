from django_filters import rest_framework as filters
from teste.models import Client, Product, Employee, Sale

# Search Filters
LIKE = 'icontains'
UNCENT = 'unaccent'
EQUALS = 'exact'
STARTS_WITH = 'startswith'
IN = 'in'
GT = 'gt'
LT = 'lt'
GTE = 'gte'
LTE = 'lte'

class ClientFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr=LIKE)
    cpf_sw = filters.CharFilter(field_name='cpf', lookup_expr=STARTS_WITH)
    cpf_equals = filters.CharFilter(field_name='cpf', lookup_expr=EQUALS)
    rg = filters.CharFilter(lookup_expr=STARTS_WITH)
    age = filters.NumberFilter(lookup_expr=EQUALS)
    class Meta:
        model = Client
        fields = ['name', 'cpf_sw', 'cpf_equals', 'rg', 'age']

class ProductFilter(filters.FilterSet):
    description = filters.CharFilter(lookup_expr=LIKE)
    quantity = filters.NumberFilter(lookup_expr=EQUALS)
    class Meta:
        model = Product
        fields = ['description', 'quantity']


class EmployeeFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr=LIKE)
    registration = filters.CharFilter(lookup_expr=STARTS_WITH)
    class Meta:
        model = Employee
        fields = ['name', 'registration']


class SaleFilter(filters.FilterSet):
    nrf = filters.CharFilter(lookup_expr=STARTS_WITH)
    id_client = filters.NumberFilter(lookup_expr=STARTS_WITH)
    id_product = filters.NumberFilter(lookup_expr=STARTS_WITH)
    id_employee = filters.NumberFilter(lookup_expr=STARTS_WITH)
    client = filters.CharFilter(field_name='client__name',lookup_expr=LIKE)
    product = filters.CharFilter(field_name='product__description',lookup_expr=LIKE)
    employee = filters.CharFilter(field_name='employee__name',lookup_expr=LIKE)

    class Meta:
        model = Sale
        fields = ['nrf', 'id_client', 'id_product', 'id_employee', 'client', 'product', 'employee']
