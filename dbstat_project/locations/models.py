from address.models import AddressField
from datetime import date
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

class locations(models.Model):
    name = models.CharField(max_length=30, unique=True)
    address = AddressField(blank=True, null=True)
    phone_number = PhoneNumberField(unique=True, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    opened = models.DateField(auto_now=False, blank=True, null=True)
    sqft = models.PositiveIntegerField(blank=True, null=True)
    number_cages = models.PositiveIntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('locations:locations-detail', kwargs={'pk': self.pk})

class positions(models.Model):
    title = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return self.title
    
class staff(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField(unique=True)
    email = models.EmailField(max_length=255, unique=True)
    position_id = models.ForeignKey(positions, on_delete=models.RESTRICT)
    
class location_staff(models.Model):
    location_id = models.ForeignKey(locations, on_delete=models.RESTRICT)
    staff_id = models.ForeignKey(staff, on_delete=models.RESTRICT)
    position_id = models.ForeignKey(positions, on_delete=models.RESTRICT)
