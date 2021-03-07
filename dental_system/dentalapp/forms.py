from django import forms
from .models import Supplier
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
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hello World'}),
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
