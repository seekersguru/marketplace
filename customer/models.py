from django.db import models
from django.contrib.auth.models import User
from api.utils import get_error as ge , get_success as gs ,req_dict
# Create your models here.
from django.db import transaction
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

"""
https://docs.djangoproject.com/en/1.8/topics/db/transactions/
Atomicity is the defining property of database transactions. atomic allows us to create a block of code within 
which the atomicity on the database is guaranteed. If the block of code is successfully completed, the changes are 
committed to the database. If there is an exception, the changes are rolled back.
"""
from django.core.signing import Signer
signer = Signer()
import random
#value = signer.sign('My string')
#original = signer.unsign(value)
#Here create Banquet Model
class Customer(models.Model):
    #email password
    user = models.OneToOneField(User, primary_key=True)
    groom_name = models.CharField(max_length=100)
    bride_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    identifier = models.CharField(max_length=512)
    tentative_wedding_date = models.CharField(max_length=20)
    fbid = models.CharField(max_length=1024,default="")
    gid =models.CharField(max_length=1024,default="")
    forgot_code =models.CharField(max_length=50,null=1)
    
    @classmethod
    @transaction.atomic # @Nishant see if its effect speed @Amit dash 
    def create(cls,
               request, 
               ):
        email = request.POST.get('email').strip().lower()
        identifier =  request.POST.get('identifier').strip().lower()
        operation =  request.POST.get('operation').strip().lower()
        password = request.POST.get('password')
        groom_name = request.POST.get('groom_name')
        bride_name = request.POST.get('bride_name')
        tentative_wedding_date = request.POST.get('tentative_wedding_date')
        contact_number = request.POST.get('contact_number').strip()
        fbid = request.POST.get("fbid","").strip()
        gid = request.POST.get("gid","").strip()
        

        ##### Get and update logic starts
        if identifier:
            customer=Customer.objects.filter(identifier=identifier)[0]
            if  operation not in ["update","get"]:
                return ge("POST",req_dict(request.POST),"Operation update or get", error_fields=['operation']) 
            if operation =="update":
                customer.groom_name=groom_name
                customer.bride_name=bride_name
                customer.contact_number=contact_number
                customer.tentative_wedding_date=tentative_wedding_date
                customer.save()

            return gs("POST",req_dict(request.POST),{"profile":{"email":customer.user.email,
                    "groom_name":customer.groom_name,
                    "bride_name":customer.bride_name,
                    "contact_number":customer.contact_number,
                    "tentative_wedding_date":str(customer.tentative_wedding_date),
                    
                    }})                 
                
         
        
        ####### Get and update logic ends

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
            customer_exist=Customer.objects.filter(user=user)
            if customer_exist:
                return ge("POST",req_dict(request.POST),"Email already exists", error_fields=['email'])
 
        if not contact_number.isdigit() :
            return ge("POST",req_dict(request.POST),"Invalid mobile number", error_fields=['contact_number'])

        if len(str(int(contact_number))) not in [10,11]:
            return ge("POST",req_dict(request.POST),"Mobile number should be of 10/11 digits", error_fields=['contact_number'])
            
        # As we using transactions, no need to error handle. 
        # In case of error all will revert
        if not user:
            user = User.objects.create_user(email, email, password)
        customer=Customer(user=user,groom_name=groom_name,
                 bride_name=bride_name,
                 contact_number=contact_number,
                 identifier=signer.sign(email),
                 fbid=fbid,
                 gid=gid)
        # do something with the book
        customer.save()
        
        return gs("POST",req_dict(request.POST),{"identifier":customer.identifier})
    
    @classmethod
    def forgot_pwd(cls,request):
        email = request.POST.get('email').strip().lower()
        user = User.objects.filter(username=email)
        if not user:
            return ge("POST",req_dict(request.POST),"Invalid username or password", error_fields=['email','password'])
            
        try:
            vendor = Customer.objects.get(user=user)
        except:
            return ge("POST",req_dict(request.POST),"User is present but problem", 
                      error_fields=['email','password'])           
        num=random.randint(10000,1000000)
        vendor.forgot_code=str(num)
        vendor.save()
        return gs("POST",req_dict(request.POST),{"num":num,"message":"A code is sent to your mail"})         

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
            customer = Customer.objects.get(user=user)
            return gs("POST",req_dict(request.POST),{"identifier":customer.identifier})

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
                      code_string="CUSTOMER_NOT_EXIST")

        else:
            user = user[0]
            customer= Customer.objects.filter(user=user)
            if customer:
                customer=customer[0]
                return gs("POST",req_dict(request.POST),{"identifier":customer.identifier})
            else:
                ## TODO Log may be user registered and is vendor else even after transaction some problem
                ## in register customer
                return ge("POST",req_dict(request.POST),
                          "User not exist", 
                          error_fields=['email','password'],
                          code_string="CUSTOMER_NOT_EXIST")                


            
            
            
            
            
            