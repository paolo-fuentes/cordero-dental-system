from django.shortcuts import render, redirect
from django.http import HttpResponse
#from dentalapp.models import Supplier
from .forms import SupplierForm
from .models import Supplier
# Create your views here.
def dentalapp(request):
    return render(request, 'dentalapp/home.html')

def supplierList(request):
    context = {'supplierList' : Supplier.objects.all()}
    return render(request,"dentalapp/SupplierList.html", context)

def supplierForm(request,id=0):
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

