from django.db import models
from vendor.models import Vendor
from customer.models import Customer
FROM_TO_CHOICES=[('v2c','v2c'), ('c2v','c2v')]        
from django import forms
from django.core.exceptions import ValidationError
from api.utils import get_error as ge , get_success as gs ,req_dict
from django.contrib.auth.models import User
MESSAGE_TYPES=["message","bid","book"]
MESSAGE_TYPES_CHOICES=[  [e,e ] for e in MESSAGE_TYPES]
print MESSAGE_TYPES_CHOICES
import datetime

class Messages(models.Model):
    vendor = models.ForeignKey(Vendor)
    customer = models.ForeignKey(Customer)
    from_to = models.CharField(max_length=3, choices=FROM_TO_CHOICES)
    message = models.TextField()
    msg_time = models.DateTimeField(auto_now_add=True)
    #
    msg_type = models.CharField(max_length=7, choices=MESSAGE_TYPES_CHOICES )
    
    book_json = models.CharField(max_length=1024,blank=True,default=None )
    event_date=models.DateField(blank=True,default=None )
    time_slot = models.CharField(max_length=128,blank=True,default=None  ) 
    bid_json = models.CharField(max_length=1024,blank=True,default=None )
    bid_price = models.CharField(max_length=100,blank=True,default=None  )    
    bid_quantity = models.IntegerField(blank=True,default=None  ) 
    status = models.CharField(max_length=1,blank=True,default=None  ) 



 
    @classmethod
    def create(cls,
               request,
               ):
        
        msg_type=request.POST.get("msg_type")
        if msg_type not in MESSAGE_TYPES:
            return ge("POST",req_dict(request.POST),"Invalid message type", error_fields=['msg_type']) 

        receiver_email = request.POST.get('receiver_email').strip().lower()
        identifier = request.POST.get('identifier')
        message = request.POST.get('message')
        from_to=request.POST.get('from_to')
        
        if msg_type in ["bid","book"] and from_to=="v2c":
            return ge("POST",req_dict(request.POST),"Vendor to Customer create not possible in bid and book", error_fields=['from_to'])
        
        
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


            
        user = User.objects.filter(username=receiver_email)
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


        event_date =request.POST.get("event_date",None)
        time_slot = request.POST.get("time_slot",None)
        bid_json = request.POST.get("bid_json","")
        book_json = request.POST.get("book_json","")
        bid_price  =request.POST.get("bid_price","").strip()  
        bid_quantity  =request.POST.get("bid_quantity","").strip()            
        if msg_type in ["bid","book"]: 
            
            try:
                event_date=datetime.date(*[int(e) for e in event_date.split("-")])
            except:
                return ge("POST",req_dict(request.POST),"Invalid event_date", error_fields=['event_date']) 

            if msg_type=="bid":
                if not bid_json:
                    return ge("POST",req_dict(request.POST),"No bid_json", error_fields=['bid_json']) 
                if bid_price:
                    try:
                        float(bid_price)
                    except:
                        return ge("POST",req_dict(request.POST),"Invalid bid_price", error_fields=['bid_price']) 
            
                if bid_quantity:
                    try:
                        int(bid_quantity)
                    except:
                        return ge("POST",req_dict(request.POST),"Invalid bid_quantity", error_fields=['bid_quantity']) 
            elif msg_type=="book":
                if not book_json:
                    return ge("POST",req_dict(request.POST),"No book_json", error_fields=['book_json']) 

        
        if not event_date:
            event_date=None
        if not  bid_quantity:
            bid_quantity=0
        msg= Messages(
               vendor=vendor,
                customer=customer,
                from_to=from_to,
                message =message,
                ## Added for bif and book
                event_date = event_date,
                time_slot = time_slot,
                bid_json = bid_json,
                book_json =book_json,
                bid_price = bid_price,
                bid_quantity =bid_quantity,
                msg_type=msg_type
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
    def vendor_bid_book_page(cls,
                        request):
        msg_type=request.POST.get('msg_type')
        msg_id=request.POST.get('msg_id')
        identifier=request.POST.get('identifier')
        if msg_type not in ["bid","book"]:
            return ge("POST",req_dict(request.POST),"msg_type can be bid / book", error_fields=['msg_type']) 
        
        vendor = Vendor.objects.filter(identifier=identifier)
        if not vendor:
            return ge("POST",req_dict(request.POST),"no message exist", error_fields=['msg_id'])
        else:
            vendor=vendor[0]
            
        msg =Messages.objects.filter(id=msg_id)
        if not ["msg"]:
            return ge("POST",req_dict(request.POST),"no message exist", error_fields=['msg_id'])
        else:
            msg=msg[0] 
        
        return {"label":"Enquiry Detail",
                "table":[{"Event Date":str(msg.event_date)},
                         {"Revenue Potential":"630++"},
                         {"Groom's Name":"Suresh"},
                         {"Bride Name":"Supriya"},
                         {"Event Date":str(msg.event_date)},
                         {"Revenue Potential":"630++"},
                         {"Groom's Name":"Suresh"},
                         {"Bride Name":"Supriya"},
                         {"Event Date":str(msg.event_date)},
                         {"Revenue Potential":"630++"},
                         {"Groom's Name":"Suresh"},
                         {"Bride Name":"Supriya"},
                         {"Event Date":str(msg.event_date)},
                         {"Revenue Potential":"630++"},
                         {"Groom's Name":"Suresh"},
                         {"Bride Name":"Supriya"},                         
                         ],
                "buttons":[["accept","Accept"],["reject","Reject"]],
                }
        
        

    @classmethod
    def details(cls,
               request, 
               ):
        msg_type=request.POST.get('msg_type')
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
            
        user = User.objects.filter(username=receiver_email)
        if not user:
            return ge("POST",req_dict(request.POST),"Receiver unauthorized", error_fields=['receiver_email'],
                      code_string="RECEIVER_NOT_EXIST")
        else:
            user=user[0]
        
        if from_to=="c2v":
            customer = sender
            vendor = receiver = Vendor.objects.filter(user=user)
        elif from_to=="v2c":
            customer = receiver = Customer.objects.filter(user=user)
            vendor = sender
            
        if not receiver:
            return ge("POST",req_dict(request.POST),"Receiver unauthorized", error_fields=['receiver_email'],
                      code_string="RECEIVERNOT_EXIST")
           
        
        
        msgs= Messages.objects.filter(
               vendor=vendor,
                customer=customer,
                msg_type=msg_type
                ).order_by('msg_time')
                
        if from_to=="c2v":       
            return gs("POST",req_dict(request.POST),[{"id":msg.id,
                                                     "message":msg.message,
                                                     "receiver_email":msg.vendor.user.username,
                                                      "vendor_name":msg.vendor.name,
                                                     "identifier":identifier,
                                                     "msg_time":str(msg.msg_time)[:19],
                                                     "from_to":msg.from_to,
                                                     "msg_type":msg_type
                                                    } for msg in msgs]) 
        elif from_to=="v2c": 
            return gs("POST",req_dict(request.POST),[{"id":msg.id,
                                                     "message":msg.message,
                                                     "receiver_email":msg.customer.user.username,
                                                      "vendor_name":msg.customer.bride_name + " vs " + msg.customer.groom_name ,
                                                     "identifier":identifier,
                                                     "msg_time":str(msg.msg_time)[:19],
                                                     "from_to":msg.from_to,
                                                     "msg_type":msg_type
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
        msg_type=request.POST.get('msg_type')
        if not sender:
            return ge("POST",req_dict(request.POST),"Sender unauthorized", error_fields=['identifier'],
                      code_string="SENDER_NOT_EXIST")
        else:
            sender=sender[0] 
            
        if from_to=="c2v":
            all_msgs= Messages.objects.filter(
                    customer=sender,msg_type=msg_type
                    ).order_by('-msg_time')
        elif from_to=="v2c":
            all_msgs= Messages.objects.filter(
                    vendor=sender,msg_type=msg_type
                    ).order_by('-msg_time')            
        
        
        msgs=[]
        listed=[]# Which vendor id indexed at which positions
        for msg in all_msgs:
            if from_to=="c2v":
                if msg.vendor.pk not in listed:
                    listed.append(msg.vendor.pk)
                    msgs.append({"id":msg.id, "message":msg.message,
                                                     "receiver_email":msg.vendor.user.username,
                                                     "receiver_name":msg.vendor.name,
                                                     "identifier":msg.customer.identifier,
                                                     "msg_time":str(msg.msg_time)[:19] ,
                                                     "from_to":msg.from_to,
                                                     "event_date":str(msg.event_date)[:19],
                                                     "msg_type":msg_type,
                                                     "line1":"Pax 350-450 Package NVS Rev:5-5100",
                                                     "line2":"Source:Wedwise",
                                                     
                                                     
                                                     })
            if from_to=="v2c":
                if msg.customer.pk not in listed:
                    listed.append(msg.customer.pk)
                    msgs.append({"id":msg.id, "message":msg.message,
                                                     "receiver_email":msg.customer.user.username,
                                                     "receiver_name":msg.customer.groom_name + " vs "+msg.customer.bride_name ,
                                                     "identifier":msg.customer.identifier,
                                                     "msg_time":str(msg.msg_time)[:19] ,
                                                     "from_to":msg.from_to,
                                                     "msg_type":msg_type,
                                                     "event_date":str(msg.event_date)[:19],
                                                     "line1":"Pax 350-450 Package NVS Rev:5-5100",
                                                     "line2":"Source:Wedwise",
                                                     })                

        

        return gs("POST",req_dict(request.POST),msgs) 


