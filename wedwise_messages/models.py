from django.db import models
from vendor.models import Vendor
from customer.models import Customer
FROM_TO_CHOICES=[('v2c','v2c'), ('c2v','c2v')]        
from django import forms
from django.core.exceptions import ValidationError
from api.utils import get_error as ge , get_success as gs ,req_dict
from django.contrib.auth.models import User

class Messages(models.Model):
    vendor = models.ForeignKey(Vendor)
    customer = models.ForeignKey(Customer)
    from_to = models.CharField(max_length=3, choices=FROM_TO_CHOICES)
    message = models.TextField()
    msg_time = models.DateTimeField(auto_now_add=True)
    
    @classmethod
    def create(cls,
               request, 
               ):
        vendor_email = request.POST.get('vendor_email').strip().lower()
        identifier = request.POST.get('identifier')
        message = request.POST.get('message')
        from_to="c2v"
     

        f = forms.EmailField()
        
        try:
            f.clean(vendor_email)
        except ValidationError:
            return ge("POST",req_dict(request.POST),"Invalid vendor email", error_fields=['vendor_email']) 
 
        customer = Customer.objects.filter(identifier=identifier)
        if not customer:
            return ge("POST",req_dict(request.POST),"Customer unauthorized", error_fields=['identifier'],
                      code_string="CUSTOMER_NOT_EXIST")
        else:
            customer=customer[0] 
            
        user = User.objects.filter(email=vendor_email)
        if not user:
            return ge("POST",req_dict(request.POST),"Vendor unauthorized", error_fields=['vendor_email'],
                      code_string="VENDOR_NOT_EXIST")
        else:
            user=user[0]
        
        vendor = Vendor.objects.filter(user=user)
        if not vendor:
            return ge("POST",req_dict(request.POST),"Vendor unauthorized", error_fields=['vendor_email'],
                      code_string="VENDOR_NOT_EXIST")
        else:
            vendor=vendor[0]            
        
        
        msg= Messages(
               vendor=vendor,
                customer=customer,
                from_to=from_to,
                message =message
                )
        msg.save()
        return gs("POST",req_dict(request.POST),{"id":msg.id,
                                                 "message":msg.message,
                                                 "vendor_email":vendor_email,
                                                 "identifier":identifier,
                                                 "msg_time":str(msg.msg_time)
                                                 })


    @classmethod
    def details(cls,
               request, 
               ):
        vendor_email = request.POST.get('vendor_email').strip().lower()
        identifier = request.POST.get('identifier')
        f = forms.EmailField()
        try:
            f.clean(vendor_email)
        except ValidationError:
            return ge("POST",req_dict(request.POST),"Invalid vendor email", error_fields=['vendor_email']) 
 
        customer = Customer.objects.filter(identifier=identifier)
        if not customer:
            return ge("POST",req_dict(request.POST),"Customer unauthorized", error_fields=['identifier'],
                      code_string="CUSTOMER_NOT_EXIST")
        else:
            customer=customer[0] 
            
        user = User.objects.filter(email=vendor_email)
        if not user:
            return ge("POST",req_dict(request.POST),"Vendor unauthorized", error_fields=['vendor_email'],
                      code_string="VENDOR_NOT_EXIST")
        else:
            user=user[0]
        
        vendor = Vendor.objects.filter(user=user)
        if not vendor:
            return ge("POST",req_dict(request.POST),"Vendor unauthorized", error_fields=['vendor_email'],
                      code_string="VENDOR_NOT_EXIST")
        else:
            vendor=vendor[0]            
        
        
        msgs= Messages.objects.filter(
               vendor=vendor,
                customer=customer,

                )
        return gs("POST",req_dict(request.POST),[{"id":msg.id,
                                                 "message":msg.message,
                                                 "vendor_email":msg.vendor.user.email,
                                                 "identifier":msg.customer.identifier,
                                                 "msg_time":str(msg.msg_time)
                                                 } for msg in msgs])    
class Book(models.Model):
    vendor = models.ForeignKey(Vendor)
    customer = models.ForeignKey(Customer)
    from_to = models.CharField(max_length=3, choices=FROM_TO_CHOICES)
    msg_time = models.DateTimeField()
    quoted_price_label= models.CharField(max_length=512) 
    message = models.TextField()


class Bid(models.Model):
    vendor = models.ForeignKey(Vendor)
    customer = models.ForeignKey(Customer)
    from_to = models.CharField(max_length=2, choices=FROM_TO_CHOICES)
    message = models.TextField()
    msg_time = models.DateTimeField()
    event_date=models.DateField()   
    quoted_price= models.CharField(max_length=512) 
    bid_price= models.FloatField() 
    quoted_price_label= models.CharField(max_length=512) 
    bid_price_entity= models.FloatField() 
    bid_price_entity_label= models.CharField(max_length=512) 

#CHOICES_VENDOR_ROLE=[('Admin','Admin'), ('Reception','Reception')] 

