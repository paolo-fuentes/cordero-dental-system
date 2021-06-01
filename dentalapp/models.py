from django.db import models
#from datetime import datetime
import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
#from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

now = timezone.now()

class Supplier(models.Model):
    contact_number=models.IntegerField(default=None)
    business_name=models.CharField(max_length=50, default=None )
    contact_person=models.CharField(unique=True, max_length=40, default=None)
    address1=models.CharField(max_length=40,  default=None)
    address2=models.CharField(max_length=40, default=None)
    special_notes=models.TextField(max_length=100, default=None)

    def __str__(self):
        return self.contact_person

class Customer(models.Model):
    customer_name=models.CharField(max_length=40, default=None)
    contact_number=models.IntegerField(default=None)
    
    def __str__(self):
        return self.customer_name

#class Delivery(models.Model):
    #supplier = models.ForeignKey(Supplier, to_field='contact_person', db_column='supplier', on_delete = models.SET_NULL, null=True)
    #delivery_date=models.DateField( default=timezone.now())
    #parcel_number = models.CharField(max_length=50, default=None)
    #materials = models.ManyToManyField('Material',through='Delivered_Material')

    #def __str__(self):
        #return str(self.supplier)

class Material(models.Model):
    def validate_date(expiry_date):
        if expiry_date < timezone.now().date():
            raise ValidationError("Date cannot be in the past")

    material_name=models.CharField(max_length=100, default=None, unique=True)
    #deliveries = models.ManyToManyField('Delivery', through='Delivered_Material')
    m_type = [
        ('Non-Perishable', 'Non-Perishable'),
        ('Perishable', 'Perishable')
    ]
    material_type = models.CharField(max_length=25, choices=m_type, default='Non-Perishable')
    expiry_date=models.DateField(default=timezone.now, validators=[validate_date], error_messages = {'required':"Invalid Date Input"})
    threshold_value = models.IntegerField(default=None)
    threshold_value_unit = models.CharField(max_length=10, default=None)
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

    # def save(self, *args, **kwargs):
    #      if self.expiry_date < datetime.date.today():
    #          raise ValidationError("The date cannot be in the past!")
    #      super(Material, self).save(*args, **kwargs)

class Delivered_Material(models.Model):

    def validate_date(delivery_date):
        if delivery_date < timezone.now().date():
            raise ValidationError("Date cannot be in the past")

    supplier = models.ForeignKey(Supplier, on_delete = models.SET_NULL, null=True)
    material = models.ForeignKey(Material,on_delete=models.SET_NULL,null=True)
    quantity_restock = models.IntegerField(default=None)
    delivery_date=models.DateField(default=timezone.now, validators=[validate_date])
    parcel_number = models.CharField(max_length=50, default=None)


    def __str__(self):
        return str(self.supplier)

    def delsupplydisplay(self):
        return str(self.quantity_restock) + " " + self.material.threshold_value_unit

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
    quantity = models.IntegerField(default=None)
    #quantity_unit = models.CharField(max_length=50, default=None)

    def __str__(self):
        return str(self.material)
    
    def rmsupplydisplay(self):
        return str(self.quantity) + " " + self.material.threshold_value_unit

class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, null=True)
    datetime = models.DateTimeField(default=timezone.now)
    status =[
    ('Scheduled','Scheduled'),
    ('Finished', 'Finished'),
    ('Cancelled','Cancelled')
    ]
    status = models.CharField(max_length=20, choices=status, default='Scheduled')

    def __str__(self):
        return (str(self.pk) +" " +str(self.customer))

class ReservationProcedure(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete = models.SET_NULL, null=True)
    procedure = models.ForeignKey(Procedure, on_delete = models.SET_NULL, null=True)

class Checkout(models.Model):
    invoice_number = models.CharField(max_length=50, default=None, null=True)
    reservation = models.ForeignKey(Reservation, on_delete = models.SET_NULL, null=True)

class ExcessMaterials(models.Model):
    excess_quantity = models.IntegerField(default=None)
    material = models.ForeignKey(Material,on_delete=models.SET_NULL,null=True)
    checkout = models.ForeignKey(Checkout,on_delete=models.SET_NULL, null=True)
    def format(self):
        return(str(self.excess_quantity)+" "+str(self.material.threshold_value_unit)+" of "+str(self.material)+" ")