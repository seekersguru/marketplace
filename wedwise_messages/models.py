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
import urllib
import datetime


class Schedulevisit(models.Model):
    vendor = models.ForeignKey(Vendor)
    customer = models.ForeignKey(Customer)
    time = models.DateTimeField()
    history = models.TextField(default="[]")
    
    
    
    @classmethod
    def create_update(cls,
               request,
               ):
        

        vendor_email = request.POST.get('vendor_email').strip().lower()
        identifier = request.POST.get('identifier')
        time = request.POST.get('time')
        if identifier:
            identifier=urllib.unquote(identifier)
        customer=Customer.objects.filter(identifier=identifier)[0]
        vendor=Vendor.objects.filter(user=User.objects.get(username=vendor_email))[0]
        sv=Schedulevisit.objects.filter(customer=customer,vendor=vendor)
        if not sv:
            history=[str(time)]
            svobj=Schedulevisit(customer=customer,vendor=vendor,time=time,history=str(history))
        else:
            svobj=sv[0]
            svobj.time=time
            svobj_history=eval(svobj.history)
            svobj_history.append(str(time))
            svobj.history=str(list(set(svobj_history)))
        svobj.save()
            


        return gs("POST",req_dict(request.POST),{"id":str(svobj.time), })  

class Messages(models.Model):
    vendor = models.ForeignKey(Vendor)
    customer = models.ForeignKey(Customer)
    from_to = models.CharField(max_length=3, choices=FROM_TO_CHOICES)
    message = models.TextField()
    msg_time = models.DateTimeField(auto_now_add=True)
    #
    msg_type = models.CharField(max_length=7, choices=MESSAGE_TYPES_CHOICES )
    
    book_json = models.TextField(blank=True,default=None )
    event_date=models.DateField(blank=True,default=None )
    time_slot = models.CharField(max_length=128,blank=True,default=None  ) 
    bid_json = models.TextField(blank=True,default=None )
    bid_price = models.CharField(max_length=100,blank=True,default=None  )    
    bid_quantity = models.IntegerField(blank=True,default=None  ) 
    status = models.CharField(max_length=1,blank=True,default=None  ) 
    self_booking = models.CharField(max_length=1,blank=True,default=None  ) 



 
    @classmethod
    def create(cls,
               request,
               ):
        
        msg_type=request.POST.get("msg_type")
        if msg_type not in MESSAGE_TYPES:
            return ge("POST",req_dict(request.POST),"Invalid message type", error_fields=['msg_type']) 

        receiver_email = request.POST.get('receiver_email').strip().lower()
        identifier = request.POST.get('identifier')
        if identifier:
            identifier=urllib.unquote(identifier)
        message = request.POST.get('message')
        from_to=request.POST.get('from_to')
        if from_to=="v2c":
            if msg_type =="bid" :
                return ge("POST",req_dict(request.POST),"Vendor to Customer create not possible in bid", error_fields=['from_to'])
            elif  msg_type =="book":
                receiver_email=identifier.split(":")[0]
                 
        
        f = forms.EmailField()
        try:
            f.clean(receiver_email)
        except ValidationError:
            return ge("POST",req_dict(request.POST),"Invalid vendor email", error_fields=['receiver_email']) 
 
        if from_to =="c2v":
            sender = Customer.objects.filter(identifier=identifier)
        elif from_to=="v2c":
            sender = Vendor.active_object.filter(identifier=identifier)
            
        if not sender:
            return ge("POST",req_dict(request.POST),"Sender unauthorized", error_fields=['identifier'],
                      code_string="SENDER_NOT_EXIST")
        else:
            sender=sender[0] 

        self_booking="0"
        if  msg_type=="book" and from_to=="v2c"  :
            #Special case
            user = [sender.user]
            self_booking="1"
        else:
            user = User.objects.filter(username=receiver_email)
        if not user:
            return ge("POST",req_dict(request.POST),"Receiver unauthorized", error_fields=['receiver_email'],
                      code_string="RECEIVER_NOT_EXIST")
        else:
            user=user[0]
        if from_to=="c2v":
            receiver = Vendor.active_object.filter(user=user)
        else: #v2c
            if msg_type=="book":
                receiver = Vendor.active_object.filter(user=user)
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
        if from_to=="v2c" and msg_type=="book":
            customer=Customer.objects.get(user=User.objects.filter(username="dummy_customer@wedwise.in")[0])
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
                msg_type=msg_type,
                self_booking=self_booking
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
    def availability(cls,request):
        year=request.POST.get('year')
        month=request.POST.get('month')
        month="%02d"%int(month)
        year_month="%s-%s"%(year,month)
        time_slot=request.POST.get('time_slot')
        avail_type=request.POST.get('avail_type')
        identifier=request.POST.get('identifier')
        dates=request.POST.get('dates')
        vendor=Vendor.active_object.filter(identifier=identifier)[0]
        if identifier:
            identifier=urllib.unquote(identifier)        
        if dates:
            if time_slot not in ["morning","evening","all_day",]:
                return ge("POST",req_dict(request.POST),"Invalid time slot", error_fields=['time_slot'])
            if avail_type not in ["available","ongoing_enquiry","booked",]:
                return ge("POST",req_dict(request.POST),"Invalid time slot", error_fields=['time_slot'])
            date_list=dates.split(",")
            #date_list = [e.split("-") for e in  dates.split(",") ]
            #Verify if proper date format
            for dt in date_list:
                dtsplt= dt.split("-")
                print datetime.date(int(dtsplt[0]),int(dtsplt[1]),int(dtsplt[2]))
            if not vendor.availability:
                vendor_availability=str({})
            else:
                vendor_availability=vendor.availability
            
            vendor_availability=eval(vendor_availability)
            for dt in date_list:
                vendor_availability[dt]=avail_type + "_"+time_slot
            vendor.availability=str(vendor_availability)
            vendor.save()
            
        data_list=[]
        if vendor.availability:
            vendor_availability=eval(vendor.availability)
            for dt, status in vendor_availability.iteritems():
                d=dt.split("-")
                if d[0] ==year and d[1]==month:
                    data_list.append({"day":d[2] , "img" :"/media/images/availability/"+status+".png"})
        return  gs("POST",req_dict(request.POST),{"data":
                                                  data_list,
                                                  "available_years":[2014,2015],
  
                                                  })


    @classmethod
    def number_bookings(cls,request):
        year=request.POST.get('year')
        month=request.POST.get('month')
        year_month="%s-%s"%(year,month)
        filter_string=request.POST.get('filter_string')
        identifier=request.POST.get('identifier')
        vendor=Vendor.active_object.filter(identifier=identifier)[0]
        messages=Messages.objects.filter(vendor=vendor)
        messages= [msg.event_date.day for msg in messages if msg.msg_type in ["bid","book"] and msg.event_date
and str(msg.event_date).startswith(year_month)
                   ]
        if identifier:
            identifier=urllib.unquote(identifier)
        from collections import Counter
        msg_counts=dict(Counter(messages))
        day_counts=[]
        for day,count in msg_counts.iteritems():
            day_counts.append({"count":count,
                                                    "day":day
                                                    })
        
        return  gs("POST",req_dict(request.POST),{"data":
                                                  day_counts,
                                                  "available_years":[2014,2015],
                                                  "book": {
                                                           "event_date": 1,
                                                           "time_slot": {
                                                                         "name": "Time Slot",
                                                                         "value": [
                                                                                   [
                                                                                    "morning",
                                                                                    "Morning"
                                                                                    ],
                                                                                   [
                                                                                    "evening",
                                                                                    "Evening"
                                                                                    ]
                                                                                   ]
                                                                         },
                                                "package": {
                                                  "name": "Package",
                                                  "value": "500 Rs per plate minimum 100 persons required"
                                                },
    "button": "BOOK"
  },
  
                                                  })
    @classmethod
    def vendor_bid_book_response(cls,request):
        identifier=request.POST.get('identifier')
        if identifier:
            identifier=urllib.unquote(identifier)
        msg_id=request.POST.get('msg_id')
        status=request.POST.get('status')
        vendor = Vendor.active_object.filter(identifier=identifier)
        if not vendor:
            return ge("POST",req_dict(request.POST),"no message exist", error_fields=['msg_id'])
        else:
            vendor=vendor[0]
            
        msg =Messages.objects.filter(id=msg_id)
        if not msg:
            return ge("POST",req_dict(request.POST),"no message exist", error_fields=['msg_id'])
        else:
            msg=msg[0] 
        msg.status=status
        msg.save()
        return  gs("POST",req_dict(request.POST),{"label":"Succesfully done"})

    @classmethod
    def vendor_bid_book_page(cls,
                        request):
        msg_type=request.POST.get('msg_type')
        msg_id=request.POST.get('msg_id')
        identifier=request.POST.get('identifier')
        if identifier:
            identifier=urllib.unquote(identifier)
        if msg_type not in ["bid",]:
            return ge("POST",req_dict(request.POST),"msg_type can be bid ", error_fields=['msg_type']) 
        
        vendor = Vendor.active_object.filter(identifier=identifier)
        if not vendor:
            return ge("POST",req_dict(request.POST),"no message exist", error_fields=['msg_id'])
        else:
            vendor=vendor[0]
            
        msg =Messages.objects.filter(id=msg_id,vendor=vendor)
        if not ["msg"]:
            return ge("POST",req_dict(request.POST),"no message exist", error_fields=['msg_id'])
        else:
            msg=msg[0] 
        if str(msg.status)=="0":
            status = "Rejected"
        elif str(msg.status)=="1":
            status = "Accepted" 
        if str(msg.status)=="2":
            status = "On Hold"
        elif str(msg.status)=="1":
            status = "Accepted" 
        else:
            status = "Pending" 
            

        """
        Contact Name
        Bride Name 
        Groom Name 
        Inquiry Date 
        Even Date 
        Time Slot 
        
        ## Event Type 
        ## Package Selected
        # of Pax 
        Potential Rev (Package Pricing)
        @Mailed to Dharam : 
   For all Vendor types 
1) Value for Event type 
2) Which fields will be hidden for which vendors.      
        
        """      
        return  gs("POST",req_dict(request.POST),{"label":"Enquiry Detail",
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
                "buttons":[["0","Accept"],["2","On Hold"],["1","Reject"]],
                "status":status
                })
        
        

    @classmethod
    def details(cls,
               request, 
               ):
        msg_type=request.POST.get('msg_type')
        receiver_email = request.POST.get('receiver_email').strip().lower()
        from_to = request.POST.get('from_to').strip().lower()
        identifier = request.POST.get('identifier')
        if identifier:
            identifier=urllib.unquote(identifier)
        f = forms.EmailField()
        try:
            f.clean(receiver_email)
        except ValidationError:
            return ge("POST",req_dict(request.POST),"Invalid receiver email", error_fields=['receiver_email']) 
 
        if from_to=="c2v":
            sender = Customer.objects.filter(identifier=identifier)
        elif from_to=="v2c":
            sender = Vendor.active_object.filter(identifier=identifier)  
            
            
            
            
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
            vendor = receiver = Vendor.active_object.filter(user=user)
        elif from_to=="v2c":
            
            if msg_type=="book":
                vendor = receiver = Vendor.active_object.filter(user=user)
                customer=None
            else:
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
        if identifier:
            identifier=urllib.unquote(identifier)
        from_to=request.POST.get('from_to')
        min=request.POST.get('min')
        max=request.POST.get('max')
        if from_to=="c2v":
            sender = Customer.objects.filter(identifier=identifier)
        elif from_to=="v2c":
            sender = Vendor.active_object.filter(identifier=identifier)
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
        
        if min:
            all_msgs=all_msgs.filter(id__lte=int(min))           
        if max:
            all_msgs=all_msgs.filter(id__gte=int(max)) 
        
        all_msgs=all_msgs[:5]         
        
        def get_status(msg):
            if str(msg.status)=="0":
                status = "Rejected"
            elif str(msg.status)=="1":
                status = "Accepted" 
            else:
                status = "Pending" 
            return status
        msgs=[]
        listed=[]# Which vendor id indexed at which positions
        for msg in all_msgs:
            event_date=str(msg.event_date)[:19]
            inquiry_date=str(msg.msg_time)[:19]
            
            if msg_type=="bid":
                inq_data=eval(msg.bid_json)
                try:
                    pkg=inq_data['quoted']['value']
                except:
                    pkg="DCR"
                line2="Pax: " + str(msg.bid_quantity)+"| Package: "+ pkg
            elif msg_type=="book":
                try:
                    inq_data=eval(msg.book_json)
                except:
                    inq_data={"quoted":{"value":"Not parsed!"}}
                try:
                    pkg=inq_data['quoted']['value']
                except:
                    pkg="DCR"
                line2="Package: "+ pkg
            elif msg_type=="message":
                line2=None
                
            if from_to=="c2v":
                line1=msg.vendor.name + "  " +event_date + "  " + inquiry_date
                if msg.vendor.pk not in listed:
                    listed.append(msg.vendor.pk)
                    msgs.append({"id":msg.id, "message":msg.message,
                                                     "receiver_email":msg.vendor.user.username,
                                                     "receiver_name":msg.vendor.name,
                                                     "identifier":msg.customer.identifier,
                                                     "msg_time":inquiry_date ,
                                                     "from_to":msg.from_to,
                                                     "event_date":event_date,
                                                     "msg_type":msg_type,
                                                     "line1":line1,
                                                     "line2":line2,
                                                     "status":get_status(msg),
                                                     
                                                     
                                                     })
            if from_to=="v2c":
                line1=msg.customer.groom_name + " & "+msg.customer.bride_name + "  " +event_date + "  " + inquiry_date
                
                if msg.customer.pk not in listed:
                    listed.append(msg.customer.pk)
                    msgs.append({"id":msg.id, "message":msg.message,
                                                     "receiver_email":msg.customer.user.username,
                                                     "receiver_name":msg.customer.groom_name + " & "+msg.customer.bride_name ,
                                                     "identifier":msg.customer.identifier,
                                                     "msg_time":inquiry_date ,
                                                     "from_to":msg.from_to,
                                                     "msg_type":msg_type,
                                                     "event_date":event_date,
                                                     "line1":line1,
                                                     "line2":line2,
                                                     "status":get_status(msg),
                                                     })                

        

        return gs("POST",req_dict(request.POST),msgs) 


