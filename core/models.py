from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=250)
    
    def __unicode__(self):
        return self.name 
    
        
class Vendor(models.Model):
    name = models.CharField(max_length=250)
    contact_number = models.CharField(max_length=50)    
    address = models.TextField()
    email = models.EmailField()
    users = models.ManyToManyField(User, through='UserMember', related_name='people')
    
    def __unicode__(self):
        return self.name    


class UserMember(models.Model):
    user = models.ForeignKey(User)
    vendor = models.ForeignKey(Vendor)
    role = models.CharField(max_length=100)
    
    def __unicode__(self):
        return "%s belong to vendor %s (as %s)" % (self.user, self.vendor, self.role)
    
    
class VendorField(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='membership')
    
    
class Fields(models.Model):    
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    length = models.IntegerField(max_length=50)
    value = models.TextField()
    
    def __unicode__(self):
        return self.name 
