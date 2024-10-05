from django.db import models
from django.db.models import Model


class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True,
    )

    active = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
    )

    created_at = models.DateTimeField(
        db_column='dt_created_at',
        auto_now_add=True,
        null=False
    )

    modified_at = models.DateTimeField(
        db_column='dt_modified_at',
        auto_now=True,
        null=False
    )

    class Meta:
        abstract = True
        managed = True

class Client(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=70,
        null=False
    )

    age = models.IntegerField(
        db_column='nb_age',
        null=False,
    )

    rg = models.CharField(
        db_column='tx_rg',
        max_length=12,
        null=False,
    )

    cpf = models.CharField(
        db_column='tx_cpf',
        max_length=12,
        null=False,
    )

class Product(ModelBase):
    description = models.CharField(
        db_column='tx_description',
        null=False
    )

    quantity = models.IntegerField(
        db_column='nb_quantity',
        null=False,
        default=0,
    )

class Employee(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=70,
        null=False,
    )

    registration = models.CharField(
        db_column='tx_registration',
        max_length=15,
        null=False,
    )

class Sale(ModelBase):
    nrf = models.CharField(
        db_column='tx_sale',
        null=False,
        max_length=255,
    )

    id_client = models.ForeignKey(Client, db_column='id_client', on_delete=models.PROTECT, null=False)

    id_product = models.ForeignKey(Product, db_column='id_product', on_delete=models.PROTECT, null=False)

    id_employee = models.ForeignKey(Employee, db_column='id_employee', on_delete=models.PROTECT, null=False)
