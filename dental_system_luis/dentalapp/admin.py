from django.contrib import admin
from .models import Supplier
from .models import Customer
#from .models import Delivery
from .models import Delivered_Material
from .models import Material
# Register your models here.

class SupplierAdmin(admin.ModelAdmin):
    list_display=['contact_number','business_name','contact_person','address1','address2','special_notes']

class CustomerAdmin(admin.ModelAdmin):
    list_display=['customer_name','contact_number']

class Delivered_MaterialAdmin(admin.ModelAdmin):
    list_display=['supplier', 'material', 'quantity_restock','delivery_date', 'parcel_number']


#class DeliveryAdmin(admin.ModelAdmin):
    #inlines = (Delivered_Material_inline,)
    #list_display=['supplier','delivery_date','parcel_number']


class MaterialAdmin(admin.ModelAdmin):
    list_display = ['material_name','current_quantity','supply_status']

#class Delivered_MaterialAdmin(admin.ModelAdmin):
    #list_display=['delivery','material']
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Customer, CustomerAdmin)
#admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Delivered_Material, Delivered_MaterialAdmin)
