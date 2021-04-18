from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
#from dentalapp.models import Supplier
from .forms import SupplierForm
from .models import Supplier
import json
from django.http import JsonResponse
from .filters import SupplierFilter
from .filters import CustomerFilter
from .filters import MaterialFilter
from .filters import DeliveryFilter
from .filters import Required_MaterialFilter
#from dentalapp.models import Customer
from .models import Customer
from .forms import CustomerForm
#from .models import Delivery
from .forms import Delivered_MaterialForm
from .forms import ProcedureForm
from .models import Delivered_Material
#from dentalapp.models import Material
from .forms import MaterialForm
from .models import Material
from .models import Procedure
from .models import Required_Material
from .forms import RequiredMaterialForm

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import ProcedureRequiredMaterialFormSet

from django.forms import inlineformset_factory

# Create your views here.
def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('dentalapp:login')

    context = {'form':form}
    return render(request, 'dentalapp/register.html', context)

def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dentalapp:dentalapp')
        else:
            messages.info(request, "Username or Password is incorrect")

    context = {}
    return render(request, 'dentalapp/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('dentalapp:login')

@login_required(login_url='dentalapp:login')
def dentalapp(request):
    return render(request, 'dentalapp/home.html')

@login_required(login_url='dentalapp:login')
def supplierList(request):
    suppliers = Supplier.objects.all()

    myFilter = SupplierFilter(request.GET, queryset=suppliers)
    suppliers = myFilter.qs


    context = {'supplierList' : suppliers, 'myFilter': myFilter}
    return render(request,"dentalapp/SupplierList.html", context)

@login_required(login_url='dentalapp:login')
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

@login_required(login_url='dentalapp:login')
def supplierDelete(request,id):
    supplier = Supplier.objects.get(pk=id)
    supplier.delete()
    return redirect('/supplierList')

@login_required(login_url='dentalapp:login')
def customerList(request):
    customers = Customer.objects.all()

    myFilter = CustomerFilter(request.GET, queryset=customers)
    customers = myFilter.qs

    context = {'customerList' : customers, 'myFilter':myFilter}
    return render(request,"dentalapp/CustomerList.html", context)

@login_required(login_url='dentalapp:login')
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

@login_required(login_url='dentalapp:login')
def customerDelete(request,id):
    customer = Customer.objects.get(pk=id)
    customer.delete()
    return redirect('/customerList')

@login_required(login_url='dentalapp:login')
def materialList(request):
    materials = Material.objects.all()

    myFilter = MaterialFilter(request.GET, queryset=materials)
    materials = myFilter.qs

    context = {'materialList' : materials, 'myFilter':myFilter}
    return render(request,"dentalapp/MaterialList.html", context)

@login_required(login_url='dentalapp:login')
def materialForm(request,id=0):
    model = Material
    form_class = MaterialForm
    if request.method == "GET":
        if id == 0: 
            form = MaterialForm()
        else:
            material = Material.objects.get(pk=id)
            form = MaterialForm(instance=material)
        return render(request,"dentalapp/MaterialForm.html",{'form':form})
    else:
        if id == 0:
            form = MaterialForm(request.POST)
        else:
            material = Material.objects.get(pk=id)
            form = MaterialForm(request.POST,instance=material)
        if form.is_valid():
            form.save()
        return redirect('/materialList')

@login_required(login_url='dentalapp:login')
def materialDelete(request,id):
    material = Material.objects.get(pk=id)
    material.delete()
    return redirect('/materialList')

@login_required(login_url='dentalapp:login')
def deliveryList(request):
    deliveries = Delivered_Material.objects.all()
    myFilter = DeliveryFilter(request.GET, queryset=deliveries)
    deliveries = myFilter.qs

    context = {'deliveryList' : deliveries, 'myFilter': myFilter}
    return render(request,"dentalapp/deliveryList.html", context)
#def deliveryForm(request):
    #form = Delivered_MaterialForm()
    #return render(request,"dentalapp/deliveryForm.html",{'form':form})

@login_required(login_url='dentalapp:login')
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

@login_required(login_url='dentalapp:login')
def deliveryDelete(request,id):
    delivery = Delivered_Material.objects.get(pk=id)
    delivery.delete()
    return redirect('/deliveryList')

#####

@login_required(login_url='dentalapp:login')
def procedureList(request):
    procedures = Procedure.objects.all()

    myFilter = MaterialFilter(request.GET, queryset=procedures)
    procedures = myFilter.qs

    context = {'procedureList' : procedures, 'myFilter':myFilter}
    return render(request,"dentalapp/procedureList.html", context)

@login_required(login_url='dentalapp:login')
def procedureForm(request,id=0):
    model = Procedure
    form_class = ProcedureForm
    if request.method == "GET":
        if id == 0: 
            form = ProcedureForm()
        else:
            procedure = Procedure.objects.get(pk=id)
            form = ProcedureForm(instance=procedure)
        return render(request,"dentalapp/ProcedureForm.html",{'form':form})
    else:
        if id == 0:
            form = ProcedureForm(request.POST)
        else:
            procedure = Procedure.objects.get(pk=id)
            form = ProcedureForm(request.POST,instance=procedure)
        if form.is_valid():
            form.save()
        return redirect('/procedureList')

@login_required(login_url='dentalapp:login')
def procedureDelete(request,id):
    procedure = Procedure.objects.get(pk=id)
    procedure.delete()
    return redirect('/ProcedureList')

def ProcedureRequiredMaterialsForm(request, pk):
    ProcedureRequiredMaterialFormSet = inlineformset_factory(Procedure, Required_Material, fields=('material', 'quantity', 'quantity_unit'), extra=10)
    procedure = Procedure.objects.get(id=pk)
    formset = ProcedureRequiredMaterialFormSet(queryset=Required_Material.objects.none(), instance=procedure)
    #form = RequiredMaterialForm(initial={'procedure':procedure})
    if request.method == 'POST':
        formset = ProcedureRequiredMaterialFormSet(request.POST, instance=procedure)
        #form = RequiredMaterialForm(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('/procedureRequiredMaterialsList')

    context = {'formset':formset}
    return render(request, "dentalapp/ProcedureRequiredMaterialForm.html", context)

def ProcedureRequiredMaterialsList(request):
    required_materials = Required_Material.objects.all()

    myFilter = Required_MaterialFilter(request.GET, queryset=required_materials)
    required_materials = myFilter.qs

    context = {'requiredMaterialList' : required_materials, 'myFilter':myFilter}
    return render(request,"dentalapp/ProcedureRequiredMaterialList.html", context)

    
    