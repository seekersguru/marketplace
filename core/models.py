from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=250)
    key = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media/vendor_image/')

    def __unicode__(self):
        return self.name 
    
        
class Vendor(models.Model):
    name = models.CharField(max_length=250)
    contact_number = models.CharField(max_length=50)    
    address = models.TextField()
    email = models.EmailField()
    category = models.ForeignKey(Category)
    
    def __unicode__(self):
        return self.name    


class VendorUser(models.Model):
    CHOICES_VENDOR_ROLE=[('Owner', 'Owner'), ('Admin','Admin'), ('Reception','Reception')]
    vendor = models.ForeignKey(Vendor)
    user = models.ForeignKey(User)
    role = models.CharField(max_length=100, choices=CHOICES_VENDOR_ROLE)
    
    def __unicode__(self):
        return "%s belong to vendor %s (as %s)" % (self.user, self.vendor, self.role)
    

class Fields(models.Model):    
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    length = models.IntegerField()
    value = models.TextField()
    
    def __unicode__(self):
        return self.name 

    
class VendorField(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='membership')
    fields = models.ForeignKey(Fields, null=True)

