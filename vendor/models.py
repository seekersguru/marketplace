from django.db import models
from api.utils import get_error as ge , get_success as gs ,req_dict
# Create your models here.

from django.db import models
from django.contrib.auth.models import User
def mode_require(request,):
    """Will make mode require from android and ios,
    Also if request says image_type is mandatory , checks that as well
    """
    #Another common operation , mode is required.
    mode=request.POST.get("mode")
    if mode not in ["android","ios"]:
        return {"error":
                response(request,ge("POST",dict(request.POST),"mode can be android or ios only",
                  error_fields=["mode"]))
                } 
    #Another common operation where mode is required ++ 
    
    image_type=request.POST.get("image_type","None")
    if image_type:
        if mode == "android" and image_type not in ALLOWED_ANDRIOD_IMAGE_TYPE:
            ## TODO Severe error 
            return  {"error":response(request,ge("POST",dict(request.POST),",".join(ALLOWED_ANDRIOD_IMAGE_TYPE) +"allowed",
                      error_fields=["mode"]))
                     }
    return {"success":{"mode":mode,"image_type":image_type}}

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
    name = models.CharField(max_length=250,)
    contact_number = models.CharField(max_length=20)
    category = models.ForeignKey(Category,)
     
    def __unicode__(self):
        return self.name


