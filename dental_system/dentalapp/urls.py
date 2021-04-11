from django.urls import path
from django.conf import settings
from . import views
from django.views.decorators.csrf import csrf_exempt


app_name = 'dentalapp'
urlpatterns = [
    path('',views.dentalapp, name='dentalapp'),
    path('supplierList',views.supplierList, name="supplier_list"),
    path('supplierForm',views.supplierForm, name="supplier_form"),
    path('<int:id>/',views.supplierForm, name='supplier_update'),
    path('supplierdelete/<int:id>/',views.supplierDelete, name='supplier_delete'),
    #path('search-supplier',csrf_exempt(views.search_supplier), name='search_supplier'),
    path('customerList',views.customerList, name="customer_list"),
    path('customerForm',views.customerForm, name="customer_form"),
    path('customer<int:id>/',views.customerForm, name='customer_update'),
    path('customerdelete/<int:id>/',views.customerDelete, name='customer_delete'),
    path('deliveryList',views.deliveryList, name="delivery_list"),
    path('deliveryForm',views.deliveryForm, name="delivery_form"),
    path('delivery<int:id>/',views.deliveryForm, name='delivery_update'),
    path('deliverydelete/<int:id>/',views.deliveryDelete, name='delivery_delete'),
    path('materialList',views.materialList, name="material_list"),
    path('materialForm',views.materialForm, name="material_form"),
    path('material<int:id>/',views.materialForm, name='material_update'),
    path('materialdelete/<int:id>/',views.materialDelete, name='material_delete')
]