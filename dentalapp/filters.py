import django_filters
from django.forms.widgets import TextInput
from .models import *

class SupplierFilter(django_filters.FilterSet):

    class Meta:
        model = Supplier
        fields = {
            'contact_person': ['icontains'],
        }


class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = {
            'customer_name': ['icontains'],
        }

class MaterialFilter(django_filters.FilterSet):
    class Meta:
        model = Material
        fields = {
            'material_name': ['icontains'],
        }

class DeliveryFilter(django_filters.FilterSet):
    class Meta:
        model = Delivered_Material
        fields = {
            'parcel_number': ['icontains'],
        }

class ProcedureFilter(django_filters.FilterSet):
    class Meta:
        model = Procedure
        fields = {
            'procedure_name': ['icontains'],
        }
