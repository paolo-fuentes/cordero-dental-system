from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

now = timezone.now()

class Supplier(models.Model):
    contact_number=models.CharField(max_length=25, default=None)
    business_name=models.CharField(max_length=50, default=None )
    contact_person=models.CharField(max_length=40, default=None)
    address1=models.CharField(max_length=40,  default=None)
    address2=models.CharField(max_length=40, default=None)
    special_notes=models.TextField(max_length=100, default=None)

