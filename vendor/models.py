from django.db import models
from api.utils import get_error as ge , get_success as gs ,req_dict
# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from api.utils import mode_require
from django import forms
from django.core.exceptions import ValidationError
from django.db import transaction
from django.core.signing import Signer
from django.contrib.auth import authenticate

signer = Signer()

VENDOR_TYPES=[("banquets","Banquets"),("caterers","Caterers"),("decorators","Decorators")
                                        ,("photographers","Photographers"),("others","Others")]
class Category(models.Model):
    name = models.CharField(max_length=250)
    key = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media/vendor_image/')

    def __unicode__(self):
        return self.name 
    @classmethod
    def get_categories(cls,request):
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
    role = models.CharField(max_length=100, choices=CHOICES_VENDOR_ROLE)
    identifier = models.CharField(max_length=512)
    fbid = models.CharField(max_length=1024,default="")
    gid =models.CharField(max_length=1024,default="")

    dynamic_info = models.TextField()

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

    @classmethod
    def login_fb_gm(cls,
               request, 
               ):
        email = request.POST.get('email').strip().lower()
        
        user=User.objects.filter(username=email)
        if not user:
            return ge("POST",req_dict(request.POST),
                      "User not exist", 
                      error_fields=['email','password'],
                      code_string="VENDOR_NOT_EXIST")

        else:
            user = user[0]
            vendor= Vendor.objects.filter(user=user)
            if vendor:
                vendor=vendor[0]
                return gs("POST",req_dict(request.POST),{"identifier":vendor.identifier})
            else:
                ## TODO Log may be user registered and is vendor else even after transaction some problem
                ## in register customer
                return ge("POST",req_dict(request.POST),
                          "User not exist", 
                          error_fields=['email','password'],
                          code_string="VENDOR_NOT_EXIST")                


    @classmethod
    def get_vendor_detail(cls,request):
        vendor_email=request.POST.get("vendor_email")
        user=User.objects.filter(username=vendor_email)
        if not user:
            return ge("POST",req_dict(request.POST),"User not exists", error_fields=['vendor_email']) 
        
        vendor = Vendor.objects.filter(user=user)  
        if not vendor:
            return ge("POST",req_dict(request.POST),"Vendor not exists", error_fields=['vendor_email']) 
        vendor=vendor[0]   
        

        data={"email":vendor.user.username,
              "name":vendor.name,
              "contact_number":vendor.contact_number,
              "address":vendor.address,
              "dynamic_info":{
                    "package_text":"",
                    "quotes_price_text":"",
                    "bid_price_label":"",
                }
         
        }
        return gs("POST",req_dict(request.POST),{"data":data})


    @classmethod
    def get_vendor_list(cls,vendor_type,page_no,mode,image_type):
        """
        Name , 
        location, 
        USP Icons,starting price , 
        starting price 
        starting price label,
        years_in_business
        others [[k1,v1], [k2,v2],....[kn.vn]]
        Banquets => min-max cap , veg only, jain only , stay ,alocohol
        """
        img="/media/apps/{mode}/{image_type}/category/{vendor_type}.jpg".\
                format(vendor_type=vendor_type,mode=mode,image_type=image_type)
        lst=[]
        for vendor in Vendor.objects.all() :
            lst.append(
                {
                 "vendor_email":vendor.user.username,
                 "image":img,
                 "name":"Name of the vendor" ,
                 "icons":[],
                 "starting_price":"500",
                 "starting_rice_labe":"Person",
                 "years_in_business":"2 years",
                 "in_favourites":3,
                 "others_two":[["Capacity","200 - 500 peoples"]],
                 "others_one":["Alcohol","Jain Only","Veg Only"],
                 },   
                )
            
        return lst
    @classmethod
    def get_listing(cls,request):

        required_mode=mode_require(request)
        if  "error" in required_mode: return required_mode["error"]
        else:
            mode= required_mode["success"]["mode"]
            image_type= required_mode["success"]["image_type"]
        
   
        
        vendor_type = request.POST.get('vendor_type').strip().lower()
        if vendor_type not in [v[0] for v in VENDOR_TYPES]:
            return ge("POST",req_dict(request.POST),"Invalid vendor type", error_fields=['vendor_type'])
        page_no = request.POST.get('page_no','')
        if not page_no: page_no="1"
     
        if not page_no.isdigit():
            return ge("POST",req_dict(request.POST),"Invalid page number", error_fields=['page_no'])
        ## TODO will do it later
        search_param= request.POST.get('search_param',"")
        if len(search_param) > 1000:
            return ge("POST",req_dict(request.POST),"search string too long", error_fields=['page_no'])
        vendor_list=cls.get_vendor_list(vendor_type,page_no,mode,image_type)
        
        return gs("POST",req_dict(request.POST),{"vendor_list":vendor_list})


    def __unicode__(self):
        return "%s belong to vendor %s (as %s)" % (self.user, self.vendor_type, self.role)

    @classmethod
    @transaction.atomic # @Nishant see if its effect speed @Amit dash 
    def update(cls,
               request, 
               ):
        try:
            import pdb;pdb.set_trace()
            email = request.POST.get('email').strip().lower()
            user=User.objects.get(username=email)
            vendor = Vendor.objects.get(user=user)
            vendor_type = request.POST.get('vendor_type').strip()
            vendor.category=Category.objects.get(key=vendor_type)
            vendor.name = request.POST.get('name').strip()
            vendor.contact_number = request.POST.get('contact_number').strip()
            vendor.address = request.POST.get('address').strip()
            vendor.dynamic_info = request.POST.get('dynamic_info').strip()
        except:
            return ge("POST",req_dict(request.POST),"Some problem in vlaues", error_fields=[]) 
        vendor.save()
        return gs("POST",req_dict(request.POST),{"id":vendor.id})
    
    @classmethod
    @transaction.atomic # @Nishant see if its effect speed @Amit dash 
    def create(cls,
               request, 
               ):
        email = request.POST.get('email').strip().lower()
        password = request.POST.get('password')
        vendor_type = request.POST.get('vendor_type')
        name = request.POST.get('name')
        contact_number = request.POST.get('contact_number').strip()
        address = request.POST.get('address').strip()
        fbid = request.POST.get("fbid","").strip()
        gid = request.POST.get("gid","").strip()        

        f = forms.EmailField()
        
        try:
            f.clean(email)
        except ValidationError:
            return ge("POST",req_dict(request.POST),"Invalid email", error_fields=['email']) 
 
        if len(password)<3:
            return ge("POST",req_dict(request.POST),"Password too short", error_fields=['password']) 
        user = User.objects.filter(username=email)

        if user:
            user=user[0]
            vendor_exist=Vendor.objects.filter(user=user)
            if vendor_exist:
                return ge("POST",req_dict(request.POST),"Email already exists", error_fields=['email'])

        if not contact_number.isdigit() :
            return ge("POST",req_dict(request.POST),"Invalid phone number", error_fields=['contact_number'])

        if len(str(int(contact_number))) < 5 or len(str(int(contact_number))) >20 :
            return ge("POST",req_dict(request.POST),"Invalid phone number", error_fields=['contact_number'])

        fbid = request.POST.get("fbid","").strip()
        gid = request.POST.get("gid","").strip() 
        dynamic_info=request.POST.get("dynamic_info","").strip()            
        # As we using transactions, no need to error handle. 
        # In case of error all will revert
        if not user:
            user = User.objects.create_user(email, email, password)
        category = Category.objects.get(key=vendor_type)
        vendor=Vendor(user=user,vendor_type=category,
                 name=name,
                 contact_number=contact_number,
                 address=address,
                 identifier=signer.sign(email),
                 fbid=fbid,
                 gid=gid,
                 dynamic_info=dynamic_info
                 )
        # do something with the book
        vendor.save()
        
        return gs("POST",req_dict(request.POST),{"identifier":vendor.identifier})

        



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


