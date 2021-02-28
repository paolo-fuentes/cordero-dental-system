from django.contrib import admin
from .models import Supplier
# Register your models here.

class SupplierAdmin(admin.ModelAdmin):
    list_display=['contact_number','business_name','contact_person','address1','address2','special_notes']

admin.site.register(Supplier, SupplierAdmin)