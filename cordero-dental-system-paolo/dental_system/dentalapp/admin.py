from django.contrib import admin
from .models import Supplier
from .models import Customer
#from .models import Delivery
from .models import Delivered_Material
from .models import Material
from .models import Procedure
from .models import Required_Material
from .models import Reservation
from .models import ReservationProcedure
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
    list_display = ['material_name', 'material_type','threshold_value_unit','threshold_value','current_quantity']


class ProcedureAdmin(admin.ModelAdmin):
    list_display = ['procedure_name', 'price']

class Required_MaterialAdmin(admin.ModelAdmin):
    list_display = ['procedure', 'material', 'quantity']

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['customer', 'datetime']

class ReservationProcedureAdmin(admin.ModelAdmin):
    list_display = ['reservation', 'procedure']

#class Delivered_MaterialAdmin(admin.ModelAdmin):
    #list_display=['delivery','material']
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Customer, CustomerAdmin)
#admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Delivered_Material, Delivered_MaterialAdmin)
admin.site.register(Procedure, ProcedureAdmin)
admin.site.register(Required_Material, Required_MaterialAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(ReservationProcedure, ReservationProcedureAdmin)

