from django.db import models
from api.utils import get_error as ge , get_success as gs ,req_dict
# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from api.utils import mode_require
from django import forms
from django.core.exceptions import ValidationError
from django.db import transaction


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
    
    

CHOICES_VENDOR_ROLE=[('Admin','Admin'), ('Reception','Reception')]        
class Vendor(models.Model):
    user = models.OneToOneField(User)
    vendor_type = models.ForeignKey(Category)
    name = models.CharField(max_length=250)
    contact_number = models.CharField(max_length=50)    
    address = models.TextField()
    email = models.EmailField()
    role = models.CharField(max_length=100, choices=CHOICES_VENDOR_ROLE)

    def __unicode__(self):
        return "%s belong to vendor %s (as %s)" % (self.user, self.vendor, self.role)
    @classmethod
    @transaction.atomic # @Nishant see if its effect speed @Amit dash 

    def create(cls,
               request, 
               ):
        email = request.POST.get('email').strip().lower()
        password = request.POST.get('password')
        vendor_type = request.POST.get('groom_name')
        name = request.POST.get('bride_name')
        contact_number = request.POST.get('contact_number').strip()
        address = request.POST.get('address').strip()
        

        f = forms.EmailField()
        
        try:
            f.clean(email)
        except ValidationError:
            return ge("POST",req_dict(request.POST),"Invalid email", error_fields=['email']) 
 
        if len(password)<3:
            return ge("POST",req_dict(request.POST),"Password too short", error_fields=['password']) 
        user = User.objects.filter(username=email)
        if user:
            return ge("POST",req_dict(request.POST),"Email already exists", error_fields=['email'])
 
        if not contact_number.isdigit() :
            return ge("POST",req_dict(request.POST),"Invalid mobile number", error_fields=['contact_number'])

        if len(str(int(contact_number))) not in [10,11]:
            return ge("POST",req_dict(request.POST),"Mobile number should be of 10/11 digits", error_fields=['contact_number'])
            
        # As we using transactions, no need to error handle. 
        # In case of error all will revert
        user = User.objects.create_user(email, email, password)
        category = Category.objects.get(key=vendor_type)
        vendor=Vendor(user=user,vendor_type=category,
                 name=name,
                 contact_number=contact_number,
                 address=address,
                 identifier=signer.sign(email))
        # do something with the book
        customer.save()
        
        return gs("POST",req_dict(request.POST),{"identifier":vendor.identifier})

        
    @classmethod
    def login(cls,
               request, 
               ):
        email = request.POST.get('email').strip().lower()
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if not user:
            return ge("POST",req_dict(request.POST),"Invalid username or password", error_fields=['email','password'])
            
        try:
            vendor = Vendor.objects.get(user=user)
            return gs("POST",req_dict(request.POST),{"identifier":vendor.identifier})

        except:
            ## TODO Proper error handling 
            ## Case 1: USer is Vendor 
            ## Case 2 : User Could not register, some error user registered but problem
            ## Critical error must be addressed TODO 
            ## Add critical error code for such situations and normal error code for all 
            return ge("POST",req_dict(request.POST),"User is present but problem", 
                      error_fields=['email','password'])


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
            return gs("POST",req_dict(request.POST),{"message":"Already in records, Wedwise team time will contact you soon."})
 
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


