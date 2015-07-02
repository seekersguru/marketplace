from django.db import models
from api.utils import get_error as ge , get_success as gs ,req_dict
# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from api.utils import mode_require
from django import forms
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=250)
    key = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media/vendor_image/')

    def __unicode__(self):
        return self.name 
    @classmethod
    def get_categories(self,request):
        required_mode=mode_require(request)
        if  "error" in required_mode: return required_mode["error"]
        else:
            mode= required_mode["success"]["mode"]
            image_type= required_mode["success"]["image_type"]
        # TODO Pick from DB
        from api.utils import ALLOWED_ANDRIOD_IMAGE_TYPE,ALLOWED_IOS_IMAGE_TYPE
        from utils import VENDOR_CATEGORIES
        host=request.get_host()
        
        data=[[
               each[1],
               str("/media/apps/%s/%s/category/%s.jpg") %(mode,image_type,each[0])
               ]
          for each in VENDOR_CATEGORIES ]
        if request.method=="POST":
            return gs("POST",req_dict(request.POST),{"data":data})
            #return ge("POST",req_dict(request.POST),"Invalid username or password", error_fields=['email','password'])
             

        
    ## TODO Discuss with Vijendra, all the images to place for now it is 
    ## Also will TODO with DATABASE entries. for all hdmi, 2x, 3x etc. have to create admin.
    
    
    
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
    name = models.CharField(max_length=100,)
    mobile = models.CharField(max_length=11,)
    address = models.CharField(max_length=512)
    services = models.CharField(max_length=512)
     
    def __unicode__(self):
        return self.name

        
    @classmethod
    def create(cls,
               request, 
               ):
        email = request.POST.get('email').strip().lower()
        name = request.POST.get('name')
        address = request.POST.get('address')
        services = request.POST.get('services')
        mobile = request.POST.get('mobile').strip()
        

        f = forms.EmailField()
        try:
            f.clean(email)
        except ValidationError:
            return ge("POST",req_dict(request.POST),"Invalid email", error_fields=['email']) 
 
        user = VendorLead.objects.filter(email=email)
        if user:
            ## TODO implement email here.
            return ge("POST",req_dict(request.POST),"Will contact you soon", error_fields=['email'])
 
        if not mobile.isdigit() :
            return ge("POST",req_dict(request.POST),"Invalid mobile number", error_fields=['mobile'])

        if len(str(int(mobile))) not in [10,11]:
            return ge("POST",req_dict(request.POST),"Mobile number should be of 10/11 digits", error_fields=['mobile'])
            
        # As we using transactions, no need to error handle. 
        # In case of error all will revert
        vendor_lead=VendorLead(email=email,name=name,
                 address=address,
                 mobile=mobile,
                 services=services)
        # do something with the book
        vendor_lead.save()
        
        return gs("POST",req_dict(request.POST),{"message":"Wedwise team time will be contacting you soon."})


