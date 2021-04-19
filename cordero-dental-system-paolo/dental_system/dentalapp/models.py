from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

now = timezone.now()

class Supplier(models.Model):
    contact_number=models.CharField(max_length=25, default=None)
    business_name=models.CharField(max_length=50, default=None )
    contact_person=models.CharField(unique=True, max_length=40, default=None)
    address1=models.CharField(max_length=40,  default=None)
    address2=models.CharField(max_length=40, default=None)
    special_notes=models.TextField(max_length=100, default=None)

    def __str__(self):
        return self.contact_person

class Customer(models.Model):
    customer_name=models.CharField(max_length=40, default=None)
    contact_number=models.CharField(max_length=25, default=None)
    
#class Delivery(models.Model):
    #supplier = models.ForeignKey(Supplier, to_field='contact_person', db_column='supplier', on_delete = models.SET_NULL, null=True)
    #delivery_date=models.DateField( default=timezone.now())
    #parcel_number = models.CharField(max_length=50, default=None)
    #materials = models.ManyToManyField('Material',through='Delivered_Material')

    #def __str__(self):
        #return str(self.supplier)

class Material(models.Model):
    material_name=models.CharField(max_length=100, default=None)
    #deliveries = models.ManyToManyField('Delivery', through='Delivered_Material')
    m_type = [
        ('Perishable', 'Perishable'),
        ('Non-Perishable', 'Non-Perishable')
    ]
    material_type = models.CharField(max_length=25, choices=m_type)
    threshold_value_unit = models.CharField(max_length=10, default=None)
    threshold_value = models.IntegerField(default=None)
    current_quantity = models.IntegerField(default=None)
    Supply =[
    ('Low','Low Supply'),
    ('Mid', 'In-Supply (Med)'),
    ('High', 'In-Supply (High)'),
    ]
    supply_status = models.CharField(max_length=20, choices=Supply)
   
    def __str__(self):
        return str(self.material_name)

    def supplydisplay(self):
        return str(self.current_quantity) + " " + self.threshold_value_unit

    def save(self, *args, **kwargs):
        if self.current_quantity>=self.threshold_value*2:
            self.supply_status = "High" 
        elif self.current_quantity>=self.threshold_value and self.current_quantity < self.threshold_value*2:
            self.supply_status = "Mid"
        else:
            self.supply_status = "Low"
        super().save(*args, **kwargs)

class Delivered_Material(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete = models.SET_NULL, null=True)
    material = models.ForeignKey(Material,on_delete=models.SET_NULL,null=True)
    quantity_restock = models.IntegerField(default=None)
    delivery_date=models.DateField(default=timezone.now)
    parcel_number = models.CharField(max_length=50, default=None)
   

    def __str__(self):
        return str(self.supplier)

    #def Updatestock(self, *args, **kwargs):
        #material_instance = self.material   # fetch the related A object in my_a
        #material_instance.current_quantity += self.quantity_restock  # update the no field of that object
        #material_instance.save()


    #post_save.connect(Updatestock, sender=Delivered_Material)
    def save(self, *arg, **kwargs):
        super(Delivered_Material, self).save(*arg, **kwargs)
        self.material.current_quantity += self.quantity_restock
        self.material.save()

class Procedure(models.Model):
    procedure_name = models.CharField(max_length=50, default=None)
    price = models.IntegerField(default=None)
    #procedure_material_name = models.ForeignKey(Material,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return str(self.procedure_name)


class Required_Material(models.Model):
    procedure = models.ForeignKey(Procedure, on_delete = models.SET_NULL, null=True, related_name='procedure_required_material')
    material = models.ForeignKey(Material,on_delete=models.SET_NULL,null=True)
    quantity = models.CharField(max_length=50, default=None)
    #quantity_unit = models.CharField(max_length=10, default=None)

    def __str__(self):
        return str(self.procedure)

