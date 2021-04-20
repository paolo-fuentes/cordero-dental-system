from django.urls import path
from django.conf import settings
from . import views
from django.views.decorators.csrf import csrf_exempt


app_name = 'dentalapp'
urlpatterns = [
    path('register/',views.registerPage, name='register'),
    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutUser, name='logout'),


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
    path('materialdelete/<int:id>/',views.materialDelete, name='material_delete'),

    path('procedureList',views.procedureList, name="procedure_list"),
    path('procedureForm',views.procedureForm, name="procedure_form"),
    path('procedure<int:id>/',views.procedureForm, name='procedure_update'),
    path('proceduredelete/<int:id>/',views.procedureDelete, name='procedure_delete'),
    path('procedureRequiredMaterialsForm<int:pk>', views.ProcedureRequiredMaterialsForm, name='procedure_required_material_form'),
    path('procedureRequiredMaterialsList<int:pk>',views.ProcedureRequiredMaterialsList, name="procedure_required_material_list"),

    path('reservationList',views.reservationList, name="reservation_list"),
    path('reservationForm',views.reservationForm, name="reservation_form"),
    path('reservation<int:id>/',views.reservationForm, name='reservation_update'),
    path('reservationdelete/<int:id>/',views.reservationDelete, name='reservation_delete'),

    path('reservationProcedureList<int:pk>',views.reservationProcedureList, name="reservationProcedure_list"),
    path('reservationProcedureForm<int:pk>',views.ReservedProceduresForm, name="reservationProcedure_form"),
    #path('reservationProcedure<int:id>/',views.ReservedProceduresForm, name='reservationProcedure_update'),
    path('reservationProceduredelete/<int:id>/',views.reservationProcedureDelete, name='reservationProcedure_delete'),


]