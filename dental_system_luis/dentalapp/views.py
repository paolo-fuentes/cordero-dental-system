from django.shortcuts import render, redirect
from django.http import HttpResponse
#from dentalapp.models import Supplier
from .forms import SupplierForm
from .models import Supplier
import json
from django.http import JsonResponse
from .models import Customer
from .forms import CustomerForm
#from .models import Delivery
from .forms import Delivered_MaterialForm
from .models import Delivered_Material



# Create your views here.
def dentalapp(request):
    return render(request, 'dentalapp/home.html')

def search_supplier(request):
    if request.method=='POST':
        search_str=json.loads(request.body).get('searchText')

        supplier = Supplier.objects.filter(contact_person__icontains=search_str)

        data = supplier.values()
        return JsonResponse(list(data), safe=False)

def supplierList(request):
    context = {'supplierList' : Supplier.objects.all()}
    return render(request,"dentalapp/SupplierList.html", context)

def supplierForm(request,id=0):
    model = Supplier
    form_class = SupplierForm
    if request.method == "GET":
        if id == 0: 
            form = SupplierForm()
        else:
            supplier = Supplier.objects.get(pk=id)
            form = SupplierForm(instance=supplier)
        return render(request,"dentalapp/SupplierForm.html",{'form':form})
    else:
        if id == 0:
            form = SupplierForm(request.POST)
        else:
            supplier = Supplier.objects.get(pk=id)
            form = SupplierForm(request.POST,instance=supplier)
        if form.is_valid():
            form.save()
        return redirect('/supplierList')

def supplierDelete(request,id):
    supplier = Supplier.objects.get(pk=id)
    supplier.delete()
    return redirect('/supplierList')

def customerList(request):
    context = {'customerList' : Customer.objects.all()}
    return render(request,"dentalapp/CustomerList.html", context)

def customerForm(request,id=0):
    model = Customer
    form_class = CustomerForm
    if request.method == "GET":
        if id == 0: 
            form = CustomerForm()
        else:
            customer = Customer.objects.get(pk=id)
            form = CustomerForm(instance=customer)
        return render(request,"dentalapp/CustomerForm.html",{'form':form})
    else:
        if id == 0:
            form = CustomerForm(request.POST)
        else:
            customer = Customer.objects.get(pk=id)
            form = CustomerForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
        return redirect('/customerList')

def customerDelete(request,id):
    customer = Customer.objects.get(pk=id)
    customer.delete()
    return redirect('/customerList')

def deliveryList(request):
    context = {'deliveryList' : Delivered_Material.objects.all()}
    return render(request,"dentalapp/deliveryList.html", context)

#def deliveryForm(request):
    #form = Delivered_MaterialForm()
    #return render(request,"dentalapp/deliveryForm.html",{'form':form})

def deliveryForm(request,id=0):
    model = Delivered_Material
    form_class = Delivered_MaterialForm
    if request.method == "GET":
        if id == 0: 
            form = Delivered_MaterialForm()
        else:
            delivery = Delivered_Material.objects.get(pk=id)
            form = Delivered_MaterialForm(instance=delivery)
        return render(request,"dentalapp/deliveryForm.html",{'form':form})
    else:
        if id == 0:
            form = Delivered_MaterialForm(request.POST)
        else:
            delivery = Delivered_Material.objects.get(pk=id)
            form = Delivered_MaterialForm(request.POST,instance=delivery)
        if form.is_valid():
            form.save()
        return redirect('/deliveryList')

def deliveryDelete(request,id):
    delivery = Delivered_Material.objects.get(pk=id)
    delivery.delete()
    return redirect('/deliveryList')