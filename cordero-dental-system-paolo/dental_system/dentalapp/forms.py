from django import forms
from .models import Supplier
from .models import Customer
from .models import Material
#from .models import Delivery
from .models import Delivered_Material
from .models import Procedure
from .models import Required_Material
from .models import Reservation
from .models import ReservationProcedure
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Checkout
from .models import ExcessMaterials

from django.forms import ModelForm, inlineformset_factory

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
        fields = ('supplier', 'material','quantity_restock', 'delivery_date', 'parcel_number')
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
        fields = ('material_name', 'material_type','threshold_value_unit','threshold_value','current_quantity', 'expiry_date')
        labels = {
            'material_name': 'Material Name',
            'material_type': 'Material Type',
            'expiry_date': 'Expiry Date',
            'threshold_value': 'Threshold Value',
            'threshold_value_unit': 'Threshold Value Unit',
            'current_quantity': 'Current Quantity',
            
        }

        m_type = [
            ('Non-Perishable', 'Non-Perishable'),
            ('Perishable', 'Perishable')
        ]

        widgets = {
            'material_name': forms.TextInput(attrs={'class': 'form-control'}),
            'material_type': forms.RadioSelect(attrs={'class': "custom-radio-list"}, choices=m_type),
            'expiry_date': forms.DateInput(attrs={'class': 'form-control'}),
            'threshold_value_unit': forms.TextInput(attrs={'class': 'form-control'}),
            'threshold_value': forms.NumberInput(attrs={'class': 'form-control', 'min':"0"}),
            'current_quantity': forms.NumberInput(attrs={'class': 'form-control', 'min':"0"}),
        }

class ProcedureForm(forms.ModelForm):
    class Meta:
        model=Procedure
        exclude = ()
        fields = ('procedure_name', 'price')
        labels = {
            'procedure_name': 'Procedure Name',
            'price': 'Price',
        }

        widgets = {
            'procedure_name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'min':"0"}),
        }

class RequiredMaterialForm(forms.ModelForm):
    class Meta:
        model = Required_Material
        fields = ('material', 'quantity')
        labels = {
            'material': 'Material',
            'quantity': 'Quantity',
        }

        widgets = {
            'material': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min':"0"}),
        }

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('customer', 'datetime')
        labels = {
            'customer': 'Customer',
            'datetime': 'Date of Appointment',
        }
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'datetime': forms.DateInput(attrs={'class': 'form-control'}),
        }

class ReservationProcedureForm(forms.ModelForm):
    class Meta:
        model = ReservationProcedure
        fields = ('procedure',)
        labels = {
            'procedure':'Procedure',
        }
        #exclude = ['procedure']
        #widgets = {
            #'procedure': forms.Select(attrs={'class': 'form-control'},choices=CHOICES),
            #'anything': forms.Select(choices=choices)
            #'datetime': forms.DateInput(attrs={'class': 'form-control'}),
        #}
    def __init__(self, *args, **kwargs):
        super(ReservationProcedureForm, self).__init__(*args, **kwargs)
        procedures = Procedure.objects.all()
        CHOICES = []
        for i in procedures:
                m=0
                x = Required_Material.objects.filter(procedure=i)
                for z in x:
                    if z.material.supply_status == 'Low':
                        m+=1
                if m==0:
                    CHOICES.append((i.procedure_name,i.procedure_name))
        print(CHOICES)
        self.fields['procedure'].choices = CHOICES

       
       
       
       
       
       
       
            # # this is pseudo code but you should get all variants
            # # then get the product related to each variant
            # #variants = Variant.objects.all()
            # #products = [(i.product.id, i.product.name) for i in variants]
            # CHOICES = []
            # for i in procedures:
            #     m=0
            #     x = Required_Material.objects.filter(procedure=i)
            #     for z in x:
            #         if z.material.supply_status == 'Low':
            #             m+=1
            #     if m==0:
            #         CHOICES.append((i.procedure_name,i.procedure_name))
            # print(CHOICES)

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ('invoice_number',)
        labels = {
            'invoice_number':'Invoice Number'
        }
        widgets = {
            'invoice_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ExcessMaterialForm(forms.ModelForm):
    class Meta:
        model = ExcessMaterials
        fields = ('material', 'excess_quantity')
        labels = {
            'material': 'Material',
            'excess_quantity': 'Excess Quantity',
        }

        widgets = {
            'material': forms.Select(attrs={'class': 'form-control'}),
            'excess_quantity': forms.NumberInput(attrs={'class': 'form-control', 'min':"0"}),
        }
#RequiredMaterialFormSet = inlineformset_factory(Procedure, Required_Material, fields=('material', 'quantity'), can_delete=True, extra=1)
ProcedureRequiredMaterialFormSet = inlineformset_factory(Procedure, Required_Material, fields=('material','quantity'))
ReservationProceduresFormSet = inlineformset_factory(Reservation, ReservationProcedure, fields=('reservation','procedure'))
ExcessMaterialsFormSet = inlineformset_factory(Checkout, ExcessMaterials, fields=('material','excess_quantity'))
