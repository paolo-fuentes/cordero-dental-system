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


    def __init__(self,*args,**kwargs):
        super(SupplierForm,self).__init__(*args, **kwargs)
        self.fields['business_name'].required=False
        self.fields['address2'].required=False
        self.fields['special_notes'].required=False
