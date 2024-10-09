from rest_framework import viewsets

from teste.filters import ClientFilter, ProductFilter, EmployeeFilter, SaleFilter
from teste.models import Client, Product, Employee, Sale
from teste.serializers import ClientSerializer, ProductSerializer, EmployeeSerializer, SaleSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filterset_class = ClientFilter


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_class = EmployeeFilter


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    filterset_class = SaleFilter
