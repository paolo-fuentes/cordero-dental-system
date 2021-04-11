import django_filters

from .models import *

class SupplierFilter(django_filters.FilterSet):
    class Meta:
        model = Supplier
        fields = {
            'contact_person': ['icontains'],
        }
        