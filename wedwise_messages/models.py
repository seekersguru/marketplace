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
        receiver_email = request.POST.get('receiver_email').strip().lower()
        identifier = request.POST.get('identifier')
        message = request.POST.get('message')
        from_to=request.POST.get('from_to')
        f = forms.EmailField()
        try:
            f.clean(receiver_email)
        except ValidationError:
            return ge("POST",req_dict(request.POST),"Invalid vendor email", error_fields=['receiver_email']) 
 
        if from_to =="c2v":
            sender = Customer.objects.filter(identifier=identifier)
        elif from_to=="v2c":
            sender = Vendor.objects.filter(identifier=identifier)
            
        if not sender:
            return ge("POST",req_dict(request.POST),"Sender unauthorized", error_fields=['identifier'],
                      code_string="SENDER_NOT_EXIST")
        else:
            sender=sender[0] 


            
        user = User.objects.filter(email=receiver_email)
        if not user:
            return ge("POST",req_dict(request.POST),"Receiver unauthorized", error_fields=['receiver_email'],
                      code_string="RECEIVER_NOT_EXIST")
        else:
            user=user[0]
        if from_to=="c2v":
            receiver = Vendor.objects.filter(user=user)
        else:
            receiver = Customer.objects.filter(user=user)
        if not receiver:
            return ge("POST",req_dict(request.POST),"Receiver unauthorized", error_fields=['receiver_email'],
                      code_string="RECEIVER_NOT_EXIST")
        else:
            receiver=receiver[0]            
        
        if from_to=="c2v":
            vendor=receiver
            customer=sender
            
        else:
            vendor=sender
            customer=receiver
            
        
        msg= Messages(
               vendor=vendor,
                customer=customer,
                from_to=from_to,
                message =message
                )
        msg.save()
        if from_to=="c2v":
            receiver_name=msg.vendor.name
        elif from_to=="v2c":
            receiver_name=msg.customer.groom_name + " weds " + msg.customer.bride_name 
        return gs("POST",req_dict(request.POST),{"id":msg.id,
                                                 "message":msg.message,
                                                 "receiver_email":receiver_email,
                                                  "receiver_name":receiver_name,
                                                 "identifier":identifier,
                                                 "msg_time":str(msg.msg_time)[:19]
                                                 })


    @classmethod
    def details(cls,
               request, 
               ):
        receiver_email = request.POST.get('receiver_email').strip().lower()
        from_to = request.POST.get('from_to').strip().lower()
        identifier = request.POST.get('identifier')
        f = forms.EmailField()
        try:
            f.clean(receiver_email)
        except ValidationError:
            return ge("POST",req_dict(request.POST),"Invalid receiver email", error_fields=['receiver_email']) 
 
        if from_to=="c2v":
            sender = Customer.objects.filter(identifier=identifier)
        elif from_to=="v2c":
            sender = Vendor.objects.filter(identifier=identifier)  
            
            
            
            
        if not sender:
            return ge("POST",req_dict(request.POST),"sender unauthorized", error_fields=['identifier'],
                      code_string="SENDER_NOT_EXIST")
        else:
            sender=sender[0] 
            
        user = User.objects.filter(email=receiver_email)
        if not user:
            return ge("POST",req_dict(request.POST),"Receiver unauthorized", error_fields=['receiver_email'],
                      code_string="RECEIVER_NOT_EXIST")
        else:
            user=user[0]
        
        if from_to=="c2v":
            receiver = Vendor.objects.filter(user=user)
            vendor = receiver
        elif from_to=="v2c":
            receiver = Customer.objects.filter(user=user)
            customer=receiver
        if not receiver:
            return ge("POST",req_dict(request.POST),"Receiver unauthorized", error_fields=['receiver_email'],
                      code_string="RECEIVERNOT_EXIST")
        else:
            receiver=receiver[0]            
        
        
        msgs= Messages.objects.filter(
               vendor=vendor,
                customer=customer,
                ).order_by('msg_time')
                
        if from_to=="c2v":       
            return gs("POST",req_dict(request.POST),[{"id":msg.id,
                                                     "message":msg.message,
                                                     "receiver_email":msg.vendor.user.email,
                                                      "vendor_name":msg.vendor.name,
                                                     "identifier":identifier,
                                                     "msg_time":str(msg.msg_time)[:19],
                                                     "from_to":msg.from_to
                                                    } for msg in msgs]) 
        elif from_to=="v2c": 
            return gs("POST",req_dict(request.POST),[{"id":msg.id,
                                                     "message":msg.message,
                                                     "receiver_email":msg.customer.user.email,
                                                      "vendor_name":msg.customer.bride_name + " vs " + msg.customer.groom_name ,
                                                     "identifier":identifier,
                                                     "msg_time":str(msg.msg_time)[:19],
                                                     "from_to":msg.from_to
                                                    } for msg in msgs])

    @classmethod
    def listing(cls,
               request, 
               ):
        identifier = request.POST.get('identifier')
        from_to=request.POST.get('from_to')
        if from_to=="c2v":
            sender = Customer.objects.filter(identifier=identifier)
        elif from_to=="v2c":
            sender = Vendor.objects.filter(identifier=identifier)
            
        
        if not sender:
            return ge("POST",req_dict(request.POST),"Sender unauthorized", error_fields=['identifier'],
                      code_string="SENDER_NOT_EXIST")
        else:
            sender=sender[0] 
            
        if from_to=="c2v":
            all_msgs= Messages.objects.filter(
                    customer=sender,
                    ).order_by('-msg_time')
        elif from_to=="c2v":
            all_msgs= Messages.objects.filter(
                    vendor=sender,
                    ).order_by('-msg_time')            
        
        
        msgs=[]
        listed=[]# Which vendor id indexed at which positions
        for msg in all_msgs:
            if from_to=="c2v":
                if msg.vendor.id not in listed:
                    listed.append(msg.vendor.id)
                    msgs.append({"id":msg.id, "message":msg.message,
                                                     "receiver_email":msg.vendor.user.email,
                                                     "receiver_name":msg.vendor.name,
                                                     "identifier":msg.customer.identifier,
                                                     "msg_time":str(msg.msg_time)[:19] ,
                                                     "from_to":msg.from_to
                                                     })
            if from_to=="v2c":
                if msg.customer.id not in listed:
                    listed.append(msg.customer.id)
                    msgs.append({"id":msg.id, "message":msg.message,
                                                     "receiver_email":msg.customer.user.email,
                                                     "receiver_name":msg.customer.groom_name + " vs "+msg.customer.bride_name ,
                                                     "identifier":msg.customer.identifier,
                                                     "msg_time":str(msg.msg_time)[:19] ,
                                                     "from_to":msg.from_to
                                                     })                

        

        return gs("POST",req_dict(request.POST),msgs) 

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

