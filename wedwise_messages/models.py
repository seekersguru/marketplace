from django.db import models
from vendor.models import Vendor
from customer.models import Customer
FROM_TO_CHOICES=[('v2c','v2c'), ('c2v','c2v')]        
from django import forms
from django.core.exceptions import ValidationError
from api.utils import get_error as ge , get_success as gs ,req_dict
from django.contrib.auth.models import User
MESSAGE_TYPES=["message","bid"]
MESSAGE_TYPES_CHOICES=[  [e,e ] for e in MESSAGE_TYPES]
import urllib
import datetime

class Schedulevisit(models.Model):
    vendor = models.ForeignKey(Vendor)
    customer = models.ForeignKey(Customer)
    time = models.DateTimeField()
    history = models.TextField(default="[]")
    
    @classmethod
    def listing(cls,
               request,
               ):
        

        identifier = request.POST.get('identifier')
        time = request.POST.get('time')
        if identifier:
            identifier=urllib.unquote(identifier)
        customer=Customer.objects.filter(identifier=identifier)[0]
        sv=Schedulevisit.objects.filter(customer=customer)
        l = [ {"vendor":schedule.vendor.name,
               "vendor_email":schedule.vendor.user.username,
                "time":str(schedule.time)
            } for schedule in sv][:50]
        

            


        return gs("POST",req_dict(request.POST),{"list":l, })    
    
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
        if not time:
            svobj=Schedulevisit.objects.filter(customer=customer,vendor=vendor)
            if svobj:
                svobj=svobj[0]
                return gs("POST",req_dict(request.POST),{"id":str(svobj.time), })  
            else:
                return gs("POST",req_dict(request.POST),{"id":"", })
        elif not sv:
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
    msg_time = models.DateTimeField(auto_now_add=True)
    vendor = models.ForeignKey(Vendor)
    customer = models.ForeignKey(Customer)
    from_to = models.CharField(max_length=3, choices=FROM_TO_CHOICES)
    message = models.TextField()
    msg_type = models.CharField(max_length=7, choices=MESSAGE_TYPES_CHOICES )
    event_date=models.DateField(blank=True,default=None )
    time_slot = models.CharField(max_length=128,blank=True,default=None  )
    package = models.CharField(max_length=256,blank=True,default=None )
    bid_json = models.TextField(blank=True,default=None )
    num_guests = models.IntegerField(blank=True,default=None  )
    notes = models.TextField(blank=True,default=None )
    status = models.CharField(max_length=1,blank=True,default=None  )
    self_booking = models.CharField(max_length=1,blank=True,default=None  )
    
    #DELETE # bid_price*** | bid_quantity*** | book_json***
    #AFTER# status
    # ADD # package*** | num_guests*** | notes
    

    @classmethod
    def delete_message(cls, request):
        from_to=request.POST.get('from_to')
        identifier=request.POST.get('identifier')
        msg_id=request.POST.get('msg_id')
        
        if from_to =="c2v":
            customer = Customer.objects.filter(identifier=identifier)
            inst =Messages.objects.filter(id=msg_id,customer=customer)
        elif from_to=="v2c":
            vendor= Vendor.active_object.filter(identifier=identifier)
            inst =Messages.objects.filter(id=msg_id,vendor=vendor)
        
        if inst:
            inst.delete()
            return gs("POST",req_dict(request.POST),{})
        else:
            return ge("POST",req_dict(request.POST),"No such message exist", error_fields=['msg_id'])
            
        
 
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
#         if from_to=="v2c":
#             if msg_type =="bid" :
#                 return ge("POST",req_dict(request.POST),"Vendor to Customer create not possible in bid", error_fields=['from_to'])
                 
        
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
        user = User.objects.filter(username=receiver_email)
        if not user:
            return ge("POST",req_dict(request.POST),"Receiver unauthorized", error_fields=['receiver_email'],
                      code_string="RECEIVER_NOT_EXIST")
        else:
            user=user[0]
        if from_to=="c2v":
            receiver = Vendor.active_object.filter(user=user)
        else: #v2c
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
        package =request.POST.get("package",None)
        num_guests = request.POST.get("num_guests","")
        notes = request.POST.get("notes","")    
        status = request.POST.get("status","") 
                    
        if msg_type in ["bid","book"]: 
            if not (package and num_guests and event_date and  time_slot):
                return "Package, Time slot , num_guests , event date are required (Server Side Check) "
            
            try:
                event_date=datetime.date(*[int(e) for e in event_date.split("-")])
            except:
                return ge("POST",req_dict(request.POST),"Invalid event_date", error_fields=['event_date']) 

            if msg_type=="bid":
                if not bid_json:
                    return ge("POST",req_dict(request.POST),"No bid_json", error_fields=['bid_json']) 
            
        
        if not event_date:
            event_date=None
        if from_to=="v2c" and msg_type=="book":
            customer=Customer.objects.get(user=User.objects.filter(username="dummy_customer@wedwise.in")[0])
        if not num_guests:
            num_guests=-1
        msg= Messages(
               vendor=vendor,
                customer=customer,
                from_to=from_to,
                message =message,
                ## Added for bif and book
                event_date = event_date,
                time_slot = time_slot,
                bid_json = bid_json,
                msg_type=msg_type,
                self_booking=self_booking,
                package=package,
                num_guests=num_guests,
                notes=notes,
                status=status
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
                try:
                    dtsplt= dt.split("-")
                    datetime.date(int(dtsplt[0]),int(dtsplt[1]),int(dtsplt[2]))
                except:
                    return ge("POST",req_dict(request.POST),"Invalid  dates", error_fields=['dates'])
            if not vendor.availability:
                vendor_availability=str({})
            else:
                vendor_availability=vendor.availability
            
            vendor_availability=eval(vendor_availability)
            blank="blank"
            for dt in date_list:
                ## 2015-09-17 booked evening
                ##print "### : ", dt , avail_type , time_slot
                if dt not in vendor_availability:
                    if time_slot=="all_day":
                        ts1,ts2=avail_type,avail_type
                    if time_slot=="morning":
                        ts1,ts2=avail_type,blank
                    if time_slot=="evening":
                        ts1,ts2=blank,avail_type
                    vendor_availability[dt]="morning-%s-evening-%s"%(ts1,ts2)
                else:
                    cur_status=vendor_availability[dt].split("-")
                    if time_slot=="all_day":
                        cur_status[1]=avail_type
                        cur_status[3]=avail_type
                    if time_slot=="morning":
                        cur_status[1]=avail_type
                    if time_slot=="evening":
                        cur_status[3]=avail_type
                    vendor_availability[dt]="-".join(cur_status)
            vendor.availability=str(vendor_availability)
            vendor.save()
            
        data_list=[]
        if vendor.availability:
            vendor_availability=eval(vendor.availability)
            for dt, status in vendor_availability.iteritems():
                d=dt.split("-")
                if d[0] ==year and d[1]==month:
                    data_list.append({"day":d[2] , "img" :"/media/images/availability/new/"+status+".png"})
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
            return ge("POST",req_dict(request.POST),"no message exist1", error_fields=['msg_id'])
        else:
            vendor=vendor[0]
        
        msg =Messages.objects.filter(id=msg_id)
        if not msg:
            return ge("POST",req_dict(request.POST),"no message exist2", error_fields=['msg_id'])
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
        from_to=request.POST.get('from_to')
        if identifier:
            identifier=urllib.unquote(identifier)
        if msg_type not in ["bid",]:
            return ge("POST",req_dict(request.POST),"msg_type can be bid ", error_fields=['msg_type']) 
        if from_to=="v2c":
            identified = Vendor.active_object.filter(identifier=identifier)
        elif from_to=="c2v":
            identified = Customer.objects.filter(identifier=identifier)

        if not identified:
            return ge("POST",req_dict(request.POST),"no message exist3", error_fields=['msg_id'])
        else:
            identified=identified[0]
        if from_to=="c2v":
            msg =Messages.objects.filter(id=msg_id,customer=identified)
        elif from_to=="v2c":
            msg =Messages.objects.filter(id=msg_id,vendor=identified)
        
        
        if not msg:
            return ge("POST",req_dict(request.POST),"no message exist4", error_fields=['msg_id'])
        else:
            msg=msg[0] 
        if str(msg.status)=="0":
            status = "Rejected"
        elif str(msg.status)=="1":
            status = "Accepted" 
        if str(msg.status)=="2":
            status = "On Hold"
        else:
            status = "Pending" 
            


        inq_data=eval(msg.bid_json)
        num_guests=str(msg.num_guests)
        try:
            package=inq_data["package"]["package_list"][msg.package]['select_val']
        except:
            err="None"
            if "package" in inq_data:
                err=str(inq_data["package"]) + ":package"
                if "package_list" in inq_data["package"]:
                    err=str(inq_data["package"]["package_list"])  + " : package_list"
                    if msg.package in inq_data["package"]["package_list"] :
                        err =str(inq_data["package"]["package_list"][msg.package]) + ": msg.package"
            package ="Invalid " + err
            print err  ,msg.package
        time_slot=[ e[1] for e in inq_data['time_slot']["value"] if e[0]==msg.time_slot ][0]
        if from_to=="c2v":
            sender_val ={"Vendor Name":msg.vendor.name}
            contact_number=msg.vendor.contact_number

        if from_to=="v2c":
            sender_val ={"Customer Name":msg.customer.contact_name}
            contact_number=msg.customer.contact_number

        msg_time=msg.msg_time
        msg_time="%s/%s/%s at %s:%s" %(str(msg_time.year),str(msg_time.month).zfill(2)
                                       ,str(msg_time.day).zfill(2) ,str(msg_time.hour).zfill(2)
                                       ,str(msg_time.minute).zfill(2))
        event_date=msg.event_date
        event_date="%s/%s/%s" %(str(event_date.day).zfill(2),str(event_date.month).zfill(2),str(event_date.year) )
        return  gs("POST",req_dict(request.POST),{"label":"Enquiry Detail",
                "contact_number":contact_number,
                "table":[#{"Event Date":str(msg.event_date)},
                         sender_val,
                         {"Groom's Name":msg.customer.groom_name},
                         {"Bride Name":msg.customer.bride_name},
                         {"Inquiry Date":msg_time  },
                         {"Event Date":event_date}, 
                         {"Package":package},
                         {"Time slot":time_slot},
                         {"# Of Guests":num_guests},
                         {"Notes ":msg.notes},

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
        min=request.POST.get('min')
        max=request.POST.get('max') 
        #sort=request.POST.get('sort')
        #Remove sorting from sevrer side, keep its client side only
        sort=""        
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
            vendor = sender
            customer =receiver =Customer.objects.filter(user=User.objects.get(username=receiver_email))[0]

                
            
        if not receiver:
            return ge("POST",req_dict(request.POST),"Receiver unauthorized", error_fields=['receiver_email'],
                      code_string="RECEIVERNOT_EXIST")
        sort_by="msg_time"  
        if sort :
            sort_by=sort
        msgs= Messages.objects.filter(
               vendor=vendor,
                customer=customer,
                msg_type=msg_type
                ).order_by("msg_time")
        if min:
            msgs=msgs.filter(id__lt=int(min))           
#         if max:
#             msgs=msgs.filter(id__gt=int(max)) 
#         if not (min or max ):
#             msgs = [e for e in msgs][-10:-5]
#         else:
        msgs = [e for e in msgs][-25:]

        
        
                         
        if from_to=="c2v":       
            return gs("POST",req_dict(request.POST),[{"id":msg.id,
                                                     "message":msg.message,
                                                     "receiver_email":msg.vendor.user.username,
                                                      "vendor_name":msg.vendor.name,
                                                     "identifier":identifier,
                                                     "msg_time":str(msg.msg_time)[:19],
                                                     "from_to":msg.from_to,
                                                     "msg_type":msg_type,
                                                     
                                                    } for msg in msgs],append="1") 
        elif from_to=="v2c": 
            return gs("POST",req_dict(request.POST),[{"id":msg.id,
                                                     "message":msg.message,
                                                     "receiver_email":msg.customer.user.username,
                                                      "vendor_name":msg.customer.bride_name.split()[-1] + " & " + msg.customer.groom_name.split()[-1] ,
                                                     "identifier":identifier,
                                                     "msg_time":str(msg.msg_time)[:19],
                                                     "from_to":msg.from_to,
                                                     "msg_type":msg_type
                                                    } for msg in msgs],append=-1)

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
        date=request.POST.get("date")
        receiver_emails=request.POST.get("receiver_emails","").strip()

        if date:
            if len(date.split("-")[0])==2:#dd-mm-yyyy
                dt=date.split("-")
                date="%s-%s-%s"%(dt[2],dt[1],dt[0])
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
                    ).order_by("msg_time")
        elif from_to=="v2c":
            if not date:
                all_msgs= Messages.objects.filter(
                        vendor=sender,msg_type=msg_type
                        ).order_by("msg_time")
            else:
                all_msgs= Messages.objects.filter(
                        vendor=sender,msg_type=msg_type,
                        event_date=datetime.datetime.strptime(date,"%Y-%m-%d")
                        ).order_by("msg_time")                
        if min and min.isdigit():
            
            if msg_type=="bid":
                all_msgs=all_msgs.filter(id__lt=int(min)) 
            else:  #msg_type=='message'
                ## TODO Memory leak issue possible here : Consider lacs of messages ) AND OVERALL
                exclude_msgs=all_msgs.filter(id__gte=int(min)) 
                all_msgs=all_msgs.filter(id__lt=int(min)) 
                ## Exclude the messages already oaded
                all_msgs = [e for e  in all_msgs if e.vendor.pk not in [i.vendor.pk for i in exclude_msgs]]
        
        if receiver_emails:
            receiver_emails=receiver_emails.split(",")
            if from_to=="v2c":
                all_msgs=[e for e in all_msgs if e.customer.user.username not in  receiver_emails][-25:]
            elif from_to=="c2v":
                all_msgs=[e for e in all_msgs if e.vendor.user.username not in  receiver_emails ][-25:]
        else:
            all_msgs=[e for e in all_msgs][-25:]  
        if msg_type=="bid":
            all_msgs.reverse()       

        def get_status(msg):
            if str(msg.status)=="0":
                status = "Rejected"
            elif str(msg.status)=="1":
                status = "Accepted" 
            elif str(msg.status)=="2":
                status = "On Hold" 
            else:
                status = "Pending" 
            return status
        msgs=[]
        sender_id_index={}
        for msg in all_msgs:
            event_date=str(msg.event_date)[:19]
            inquiry_date=str(msg.msg_time)[:19]
            
            if msg_type=="bid":
                inq_data=eval(msg.bid_json)

                try:
                    package=inq_data["package"]["package_list"][msg.package]['select_val']
                except:
                    package="Not specified"
                    
                try:
                    
                    revenue=inq_data["package"]["package_list"][msg.package]["price"]
                    revenue=str(float(revenue))
                    if msg.num_guests:
                        revenue=" Rs." + str(revenue*int(msg.num_guests))  ;
                except:
                    revenue="Not good for till time"

                time_slot=[ e[1] for e in inq_data['time_slot']["value"] if e[0]==msg.time_slot.replace(" ","").lower() ][0]
                if from_to=="c2v":
                    line11,line12,line13 = package , " ", time_slot
                    line21,line22,line23= revenue , " ", get_status(msg)
                elif from_to=="v2c":
                    line11,line12,line13 = package , str(msg.num_guests),time_slot
                    line21,line22,line23= revenue , " ", get_status(msg)
            elif msg_type=="message":
                line11=line12=line13=line21=line22=line23=""
                
                
            msg_detail = {"id":msg.id, "message":msg.message,
                                                 "receiver_email":from_to=="c2v" and msg.vendor.user.username or msg.customer.user.username,
                                                 "receiver_name":from_to=="c2v" and msg.vendor.name or msg.customer.groom_name + " & "+msg.customer.bride_name,
                                                 "msg_time":inquiry_date ,
                                                 "msg_time_only":inquiry_date.split()[1][:5] ,
                                                 "from_to":msg.from_to,
                                                 "event_date":event_date,
                                                 "msg_type":msg_type,
                                                 "line1":str(line11) + "|"+str(line12) + str(line13),
                                                 "line2":str(line21) + "|"+str(line22) + str(line23),
                                                 "status":get_status(msg),
                                                 "line11":line11,
                                                 "line12":line12,
                                                 "line13":line13,
                                                 "line21":line21,
                                                 "line22":line22,
                                                 "line23":line23
                                                 
                                                 } 
            if msg_type=="bid"  :
                
                
                msgs.append(msg_detail)
            else: #msg_type=="message"
                if from_to =="c2v":
                    sender_id=msg.vendor.pk
                elif from_to=="v2c":
                    sender_id=msg.customer.pk
                
                if sender_id not in sender_id_index:
                    sender_id_index[sender_id]=len(msgs)
                    msgs.append(msg_detail) 
                else:# Retainings
                    msgs[sender_id_index[sender_id]]=msg_detail
                  


        if msg_type=="bid":
            append="1"
        if msg_type=="message":
            append="-1"        

            
        return gs("POST",req_dict(request.POST),msgs,append=append) 


