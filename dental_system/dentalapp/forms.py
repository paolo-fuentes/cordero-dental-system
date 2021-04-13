from django import forms
from .models import Supplier
from .models import Customer
from .models import Material
#from .models import Delivery
from .models import Delivered_Material
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SupplierForm(forms.ModelForm):
    class Meta:
        model=Supplier
        fields = ('contact_number','business_name','contact_person','address1','address2','special_notes')
        labels = {
            'contact_number': 'Contact Number',
            'business_name': 'Business Name',
            'contact_person': 'Contact Person',
            'address1': 'Address Line 1',
            'address2': 'Address Line 2',
            'special_notes': 'Special Notes'
        }

        widgets = {
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'business_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_person': forms.TextInput(attrs={'class': 'form-control'}),
            'address1': forms.TextInput(attrs={'class': 'form-control'}),
            'address2': forms.TextInput(attrs={'class': 'form-control'}),
            'special_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


    def __init__(self,*args,**kwargs):
        super(SupplierForm,self).__init__(*args, **kwargs)
        self.fields['business_name'].required=False
        self.fields['address2'].required=False
        self.fields['special_notes'].required=False

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields = ('customer_name','contact_number')
        labels = {
            'customer_name': 'Customer Name',
            'contact_number': 'Contact Number',
        }

        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

class Delivered_MaterialForm(forms.ModelForm):
    class Meta:
        model=Delivered_Material
        fields = ('supplier', 'material','quantity_restock', 'delivery_date','parcel_number')
        labels = {
            'supplier': 'Supplier',
            'material': 'Delivered Material',
            'quantity_restock': 'Restock Quantity',
            'delivery_date': 'Delivery Date',
            'parcel_number': 'Parcel Number',
        }

        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'material': forms.Select(attrs={'class': 'form-control'}),
            'quantity_restock': forms.NumberInput(attrs={'class': 'form-control', 'min':"0"}),
            'delivery_date': forms.DateInput(attrs={'class': 'form-control'}),
            'parcel_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self,*args,**kwargs):
        super(Delivered_MaterialForm,self).__init__(*args, **kwargs)
        self.fields['parcel_number'].required=False

class MaterialForm(forms.ModelForm):
    class Meta:
        model=Material
        fields = ('material_name', 'material_type','threshold_value_unit','threshold_value','current_quantity')
        labels = {
            'material_name': 'Material Name',
            'material_type': 'Material Type',
            'threshold_value_unit': 'Threshold Value Unit',
            'threshold_value': 'Threshold Value',
            'current_quantity': 'Current Quantity',
        }

        widgets = {
            'material_name': forms.TextInput(attrs={'class': 'form-control'}),
            'material_type': forms.Select(attrs={'class': 'form-control'}),
            'threshold_value_unit': forms.TextInput(attrs={'class': 'form-control'}),
            'threshold_value': forms.NumberInput(attrs={'class': 'form-control', 'min':"0"}),
            'current_quantity': forms.NumberInput(attrs={'class': 'form-control', 'min':"0"}),
        }
