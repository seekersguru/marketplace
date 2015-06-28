from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=250)
    key = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media/vendor_image/')

    def __unicode__(self):
        return self.name 
    
CHOICES_VENDOR_ROLE=[('Owner', 'Owner'), ('Admin','Admin'), ('Reception','Reception')]        
class Vendor(models.Model):
    user = models.OneToOneField(User)
    vendor = models.ForeignKey(Category)
    name = models.CharField(max_length=250)
    contact_number = models.CharField(max_length=50)    
    address = models.TextField()
    email = models.EmailField()
    role = models.CharField(max_length=100, choices=CHOICES_VENDOR_ROLE)
    def __unicode__(self):
        return "%s belong to vendor %s (as %s)" % (self.user, self.vendor, self.role)


class VendorLead(models.Model):
    #email password
    email = models.EmailField()
    name = models.CharField(max_length=250,)
    contact_number = models.CharField(max_length=20)
    category = models.ForeignKey(Category,)
     
    def __unicode__(self):
        return self.name


