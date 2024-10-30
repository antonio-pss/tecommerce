from django.http import JsonResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from teste.filters import ClientFilter, ProductFilter, EmployeeFilter, SaleFilter
from teste.models import Client, Product, Employee, Sale
from teste.serializers import ClientSerializer, ProductSerializer, EmployeeSerializer, SaleSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filterset_class = ClientFilter
    # permission_classes = {permissions.IsAuthenticated}

    @action(detail=False, methods=['GET'])
    def antonios(self, request, *args, **kwargs):
        # Aqui usamos o serializer, pois ele serve para transformar um objeto em json.
        clients = Client.objects.get(id=1)
        cd_serializer = self.get_serializer(clients)
        return Response(cd_serializer.data, status=200)


    """
    @action(detail=False, methods=['GET'])
    def antonios(self, request, *args, **kwargs):
        # Aqui usamos o values retornando um queryset em formato já json.
        clients = Client.objects.filter(name__icontains='Antô').values()
        return Response(clients, status=200)
    """

    """
    # Funções inbuilt que podemos utilizar para requisições web.
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    """

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    # permission_classes = {permissions.IsAuthenticated}


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_class = EmployeeFilter
    # permission_classes = {permissions.IsAuthenticated}


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    filterset_class = SaleFilter
    # permission_classes = {permissions.IsAuthenticated}
