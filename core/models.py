from django.db import models
from django.contrib.auth.models import User


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=100)
    address = models.TextField()
    users = models.ManyToManyField(User, through='UserMember', related_name='people')
    
    def __unicode__(self):
        return self.name    


class UserMember(models.Model):
    user = models.ForeignKey(User)
    vendor = models.ForeignKey(Vendor)
    role = models.CharField(max_length=100)
    
    def __unicode__(self):
        return "%s belong to vendor %s (as %s)" % (self.user, self.vendor, self.role)
    
    
class VendorDetail(models.Model):
    type = models.CharField(max_length=50)
    data_dict = models.TextField()
    vendor = models.ForeignKey(Vendor, related_name='membership')
