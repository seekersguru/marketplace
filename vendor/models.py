from django.db import models
from api.utils import get_error as ge , get_success as gs ,req_dict
# Create your models here.
import json
from django.db import models
from django.contrib.auth.models import User
from api.utils import mode_require
from django import forms
from django.core.exceptions import ValidationError
from django.db import transaction
from django.core.signing import Signer
from django.contrib.auth import authenticate
import random
import urllib
from customer.models import Customer
from django.template.defaultfilters import default
from manager import VendorManager
from __builtin__ import classmethod

signer = Signer()


class Category(models.Model):
    name = models.CharField(max_length=250)
    key = models.CharField(max_length=250)
    #image = models.ImageField(upload_to='media/vendor_image/')

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
    

VENDOR_TYPES=[(e.name,e.name) for e in Category.objects.all()]



    

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
    forgot_code =models.CharField(max_length=50,blank=True, null=True)
    availability = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=1)
    
    objects = models.Manager()
    active_object = VendorManager()



    @classmethod
    def locations(cls,request):
        locs=["Mira Road", "Chembur", "Andheri West", "Kharghar", "Malad West", "Andheri East", "Bandra West", "Goregaon West", "Kandivali East", "Ghodbunder Road", "Navi Mumbai", "Bhandup West", "Borivali West", "Panvel", "Khar East", "Kandivali West", "Goregaon East", "90 Feet Road", "Nelson Manickam Road", "Abdul Rehman Street", "Agripada", "Airoli", "Airoli Sector 4", "Airoli Sector 8", "Altamount Road", "Ambarnath", "Ambarnath East", "Ambernath West", "Amboli", "Andheri Kurla Road", "Andheri Sahar Road", "Antop Hill", "Apollo Bunder", "August Kranti Maidan", "Babulnath Road", "Badlapur", "Ballard Estate", "Bandra East", "Belapur", "Bhandup", "Bhandup East", "Bhayandar", "Bhayandar East", "Bhayandar Wada", "Bhayandar West", "Bhayander", "Bhayander East", "Bhayander West", "Bhindi Bazaar", "Bhiwandi", "Bhiwandi", "Bhoiwada", "Bhulabhai Desai Road", "Bhuleshwar", "Bhyandar East", "Boisar", "Boisar West", "Borivali", "Borivali East", "Breach Candy", "Byculla", "Byculla East", "Byculla West", "Cp Tank", "Chhatrapati Shivaji Terminus", "Carnac Bunder", "Cbd Belapur", "Cbd Belapur Sector 11", "Chakala", "Chandivali", "Charkop", "Charni Road", "Charni Road East", "Chembur Camp", "Chembur Colony", "Chembur East", "Chembur West", "Chinch Bandar", "Chinch Bunder", "Chinchpokli", "Chinchpokli East", "Chinchpokli West", "Chira Bazaar", "Chowpatti", "Chuna Bhatti", "Churchgate", "Colaba Causeway", "Cotton Green", "Cotton Green West", "Crawford Market", "Cuffe Parade", "Cumbala Hill", "Currey Road", "Dadabhai Naoroji Road", "Dadar East", "Dadar T T", "Dadar West", "Dahisar", "Dahisar East", "Dahisar West", "Dana Bunder", "Delisle Road", "Deonar", "Deonar East", "Dharavi", "Dhobhi Talao", "Dhobi Talao", "Dockyard", "Dombivali", "Dombivali East", "Dombivali West", "Dongri", "Elphinstone Road", "Flora Fountain", "Fort", "Gamdevi", "Ghansoli", "Ghatkopar", "Ghatkopar East", "Ghatkopar West", "Ghodbandar Road", "Girgaon", "Girgaon Chowpatty", "Girgaum", "Goregaon East", "Goregaon West", "Govandi", "Govandi East", "Govandi West", "Gowalia Tank", "Grant Road", "Grant Road East", "Grant Road West", "Green Park Extension", "Gulalwadi", "Haji Ali", "Horiman Circle", "Hughes Road", "Hutatma Chowk", "J B Nagar", "Jacob Circle", "Jogeshwari", "Jogeshwari East", "Jogeshwari West", "Juhu Scheme", "Juhu Tara Road", "Kalachowki", "Kala Ghoda", "Kalamboli", "Kalbadevi", "Kalina", "Kalwa", "Kalwa West", "Kalyan", "Kalyan East", "Kalyan West", "Kamothe", "Kandivali", "Kanjur Marg East", "Kanjur Marg West", "Kanjurmarg", "Kanjurmarg East", "Kanjurmarg West", "Kazi Sayed Street", "Kemps Corner", "Khar", "Khar Danda", "Khar West", "Kharghar Sector 12", "Kharghar Sector 2", "Kharghar Sector 7", "Khetwadi", "Khopoli", "Kings Circle", "Kopar Khairane", "Koper Khraine", "Andheri Kurla Road", "Kurla East", "Kurla West", "Lal Bahadur Shastri Marg", "Lal Baug", "Lalbaug", "Lamington Road", "Lbs Marg", "Link Road", "Lohar Chawl", "Lokhandwala", "Parel", "Lower Parel East", "Lower Parel West", "M G Road", "Mahakali Caves Road", "Mahalaxmi", "Mahalaxmi West", "Mahape", "Mahim", "Mahim East", "Mahim West", "Malabar Hill", "Aarey Milk Colony", "Airport", "Ambewadi", "Andheri", "Asvini", "Azad Nagar", "Bpt Colony", "Bn Bhavan", "Bandra", "Bazargate", "Bharat Nagar", "Bhavani Shankar Road", "Cgs Colony", "Air India Staff Colony", "Century Mills Worli", "Chamar Baug", "Colaba", "Cotton Exchange", "Dadar Colony", "Dadar", "Danda", "Dockyard Road", "Dr Deshmukh Marg", "Falkland Road", "Girgaon Mdg", "Gokhale Road", "Goregoan", "Government Colony", "Hmp School", "Haffkine Institute", "Haines Road", "Hanuman Road", "High Court Building", "Holiday Camp", "Ins Hamla", "Central Building", "Parel Naka", "Oshiwara", "Opera House", "New Yogakshema", "New Prabhadevi Road", "N S Patkar Marg", "Mori Road", "Mazgaon Road", "Jj Hospital", "Juhu", "Kamathipura", "Ketkipada", "Kherwadi", "Kidwai Nagar", "Liberty Garden", "Mazagon Dock", "Naigaon", "Mumbai Central", "Orlem", "Nagardas Road", "Madhavbaug", "Khar Delivery", "Mpt", "M A Marg", "Magathane", "Lbsne College", "Mazagaon", "Matunga Railway Workshop", "Motilal Nagar", "Nariman Point", "International Airport", "Irla", "Malad", "Mantralaya", "Marine Lines", "Marol Naka", "Prabhadevi", "Princess Dock", "Raj Bhavan", "Rajendra Nagar", "Ramwadi", "Ranade Road", "Rani Sati Marg", "Srpf Camp", "S Savarkar Marg", "S.K. Nagar", "Sahar Pt Colony", "Sahargaon", "Santacruz Central", "Santacruz P And T Colony", "Santacruz", "Secretariat", "Seepz", "Sewri", "Sharma Estate", "Shroffmahajan", "Shroff Mahajan", "Stock Exchange", "Tajmahal", "Tajmahal Hotel", "Tank Road", "Tardeo", "Taj Mahal Hotel", "Thakurdwar", "Town Hall", "Tulsiwadi", "Vjb Udyan", "Vk Bhavan", "Vp Road", "Vwtc", "Vakola", "Vesava", "Vidyanagari", "Vileeparle", "Vile Parle", "Wadala", "Worli", "Ambarnath West", "Kharghar"]
        match_string=request.POST.get("match_string","")
        if match_string:
            locs = [e for e in locs if match_string.lower() in e.lower()]
        return gs("POST",req_dict(request.POST),{"locations":locs , "version":1})
    @classmethod
    def get_locations_version(cls,request):
        return gs("POST",req_dict(request.POST),{"version":1 , })    
    
    @classmethod
    def check_availability(cls,
               request,
               ):
        

        vendor_email = request.POST.get('vendor_email').strip().lower()
        identifier = request.POST.get('identifier')
        time_slot = request.POST.get('time_slot')
        event_date = request.POST.get('event_date')
        

        if identifier:
            identifier=urllib.unquote(identifier)
        customer=Customer.objects.filter(identifier=identifier)[0]
        vendor=Vendor.objects.filter(user=User.objects.get(username=vendor_email))[0]
        try:
            availability=eval(vendor.availability).get(str(event_date))
        except:
            availability=None
        if availability \
            and availability.startswith("booked_"):

            ts_stored=availability.split("booked_")[1]
            available=1
            if ts_stored=="all_day":
                available=0 
            if ts_stored==time_slot:
                available=0
            if available ==0:
                return gs("POST",req_dict(request.POST),{"available":0, })  
            if time_slot =="all_day":
                return gs("POST",req_dict(request.POST),{"available":0, }) 
                
        
        return gs("POST",req_dict(request.POST),{"available":1, })  
    
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
            if Vendor.objects.get(user=user):
                try:    
                    vendor = Vendor.active_object.get(user=user)
                    return gs("POST",req_dict(request.POST),{"identifier":vendor.identifier})
                except: 
                    return ge("POST",req_dict(request.POST),"Please wait for admin to approve.", 
                              error_fields=['email','password'])
        except:
            ## TODO Proper error handling 
            ## Case 1: USer is Vendor 
            ## Case 2 : User Could not register, some error user registered but problem
            ## Critical error must be addressed TODO 
            ## Add critical error code for such situations and normal error code for all 
            return ge("POST",req_dict(request.POST),"User is present but problem1", 
                      error_fields=['email','password'])

    @classmethod
    def forgot_pwd(cls,request):
        email = request.POST.get('email').strip().lower()
        user = User.objects.filter(username=email)
        if not user:
            return ge("POST",req_dict(request.POST),"Invalid username or password", error_fields=['email','password'])
            
        try:
            vendor = Vendor.active_object.get(user=user)
        except:
            return ge("POST",req_dict(request.POST),"User is present but problem2", 
                      error_fields=['email','password'])           
        num=random.randint(10000,1000000)
        vendor.forgot_code=str(num)
        vendor.user.set_password(str(num))
        vendor.user.save()
        return gs("POST",req_dict(request.POST),{"num":num,"message":str(num) + "Password sent to your mail"})

    @classmethod
    def reset_pwd(cls,request):
        email = request.POST.get('email').strip().lower()
        code = request.POST.get('code').strip().lower()
        password = request.POST.get('password') 
        confirm_password = request.POST.get('confirm_password') 
        
        user = User.objects.filter(username=email)
        if not user:
            return ge("POST",req_dict(request.POST),"Invalid username or password", error_fields=['email','password'])
            
        try:
            vendor = Vendor.object.get(user=user)
        except:
            return ge("POST",req_dict(request.POST),"User is present but problem3", 
                      error_fields=['email','password'])  
            
        if str(vendor.forgot_code) != str(code).strip():
            return ge("POST",req_dict(request.POST),"Code mismatch", 
                      error_fields=['code',]) 
        if password !=confirm_password:
            return ge("POST",req_dict(request.POST),"Password and confor==irm password mismatch", 
                      error_fields=['email','password']) 
        user.set_password(password)
        user.save()
        return gs("POST",req_dict(request.POST),{"message":"Password reset succesful"})    
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
        identifier = request.POST.get('identifier',"").strip().lower()  
        customer=None
        if identifier:
            identifier=urllib.unquote(identifier)
            customer=Customer.objects.filter(identifier=identifier)[0]
        favorite="-1"
        if customer:
            from customer.models import Favorites
            fav=Favorites.objects.filter(customer=customer,
                            vendor=Vendor.active_object.get(user=User.objects.get(username=vendor_email))
                            )
            if fav and fav[0].favorite=="1":
                favorite="1"
            
        if not user:
            return ge("POST",req_dict(request.POST),"User not exists", error_fields=['vendor_email']) 
        user=user[0]
       
        vendor = Vendor.active_object.filter(user=user)  
        if not vendor:
            return ge("POST",req_dict(request.POST),"Vendor not exists", error_fields=['vendor_email']) 
        vendor=vendor[0]  
        data = json.loads(vendor.dynamic_info) 
        data["favorite"]=favorite
        return gs("POST",req_dict(request.POST),{"data":data})

    @classmethod
    def get_favorites(cls,customer):
        from customer.models import Favorites
        
        return dict([(obj.vendor.user.username,obj.favorite) for obj in Favorites.objects.filter(customer=customer)])
    
    @classmethod
    def get_vendor_list(cls,page_no,mode,image_type,vendor_type=None,search_string=None,favorites=None,customer=None):
        from customer.models import Favorites

        img="/media/apps/{mode}/{image_type}/category/{vendor_type}.jpg".\
                format(vendor_type=vendor_type,mode=mode,image_type=image_type)
        lst=[]
        cust_favorites=cls.get_favorites(customer)

        if favorites=="1":
            fav_list=Favorites.objects.filter(customer=customer)
            ven_list=[fav.vendor for fav in fav_list]
            
        else:
            ven_list=Vendor.active_object.filter(vendor_type=Category.objects.get(key=vendor_type))
        if search_string:
            ven_list=[e for e in ven_list if search_string.lower() in e.dynamic_info.lower()] 
          
        for vendor in ven_list :
                
            lst.append(
                {
                 "vendor_email":vendor.user.username,
                 "image":img,
                 "name":vendor.name ,
                 "favorite":cust_favorites.get(vendor.user.username,"-1"),
                 #todo make it dynamic
                 "icons_line1":[
                        {"/media/icons/2x/icon1.png":"Alcohol"},
                        {"/media/icons/2x/icon2.png":"Parking"},               
                ],
                 "icons_line2":[
                        {"/media/icons/2x/icon3.png":"DJ"},
                        {"/media/icons/2x/icon4.png":"MM"},               
                ],               
                 "starting_price":"500",
                 "starting_rice_label":"Person",
                 "years_in_business":"2 years",
                 "in_favourites":3,
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
        
        favorites= request.POST.get('favorites',"")
        if not favorites=="1":
            vendor_type = request.POST.get('vendor_type')
            if vendor_type not in [v[1] for v in VENDOR_TYPES]:
                return ge("POST",req_dict(request.POST),"Invalid vendor type", error_fields=['vendor_type'])
            vendor_type=Category.objects.get(name=vendor_type).key
        page_no = request.POST.get('page_no','')
        if not page_no: page_no="1"
     
        if not page_no.isdigit():
            return ge("POST",req_dict(request.POST),"Invalid page number", error_fields=['page_no'])
        ## TODO will do it later
        search_string= request.POST.get('search_string',"")

        if len(search_string) > 1000:
            return ge("POST",req_dict(request.POST),"search string too long", error_fields=['page_no'])

        identifier = request.POST.get('identifier',"").strip().lower()  
        customer=None
        if identifier:
            identifier=urllib.unquote(identifier)
            customer=Customer.objects.filter(identifier=identifier)[0]         
        if not favorites=="1":
            vendor_list=cls.get_vendor_list(page_no,mode,image_type,search_string=search_string,vendor_type=vendor_type,favorites=favorites,customer=customer,)
        else:
            vendor_list=cls.get_vendor_list(page_no,mode,image_type,search_string=search_string,favorites="1",customer=customer)



        return gs("POST",req_dict(request.POST),{"vendor_list":vendor_list ,                 
                    "venue_type":
                        {
                            "name": "Venue Type",
                            "value": [
                                [
                                    "hotel",
                                    "Hotel"
                                ],
                                [
                                    "banquet",
                                    "Banquet"
                                ],
                            ]
                        },
                    "pricing":{
                        "name": "Price Range",
                        "value": [
                            [
                                "<200",
                                "Less than 00 Rs."
                            ],
                            [
                                "200-500",
                                "200-500 Rs"
                            ],
                            [
                                ">500",
                                "More than 500 Rs"
                            ],
                        ]
                    },
            })



    def __unicode__(self):
        return "%s belong to vendor %s (as %s)" % (self.user, self.vendor_type, self.role)

    @classmethod
    @transaction.atomic # @Nishant see if its effect speed @Amit dash 
    def update(cls,
               request, 
               ):
        try:
            email = request.POST.get('email').strip().lower()
            user=User.objects.get(username=email)
            vendor = Vendor.active_object.get(user=user)
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


