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
    path('delete/<int:id>/',views.supplierDelete, name='supplier_delete'),
    path('search-supplier',csrf_exempt(views.search_supplier), name='search_supplier'),
]