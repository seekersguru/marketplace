from django.template.response import TemplateResponse
from urls import patterns
from django.views.decorators.csrf import csrf_exempt
from collections import OrderedDict

from api.utils import get_error as ge , get_success as gs
import json
from django.http import HttpResponse


def check_basic_validations(pattern_name,request,req_type):
    required=patterns[pattern_name].get("required_params",None)
    if req_type =="POST":
        data=request.POST
    elif req_type =="GET":
        data=request.GET
    req_missing=[]
    for each in required:
        if not data.get(each):
            req_missing.append(each)
            
    if req_missing:
        return ge("POST",data,"required fields missing",
                  json_data=req_missing)    

def response(request,res):
    return  HttpResponse(json.dumps(res), content_type="application/json")
    #return TemplateResponse(request,'api/api.html',{"res":res})

def index(request):
    lst=[ (k,v) for k,v in patterns.iteritems()]
    lst=OrderedDict(sorted(lst, key= lambda e:e[1]['order']))
    return TemplateResponse(request,'api/api_index.html',
                {"patterns":lst})

########## Customer Login Registration
@csrf_exempt
def customer_registration(request):
    invalid=check_basic_validations("customer_registration",request,"POST")
    if invalid:return response(request,invalid) 
    from customer.models import Customer
    res={}
    if request.method=="POST":
        res=Customer.create(request)
    
    
def customer_login(request):
    return TemplateResponse(request,'api/api.html',{})
def customer_registration_login_fb(request):
    return TemplateResponse(request,'api/api.html',{})
def customer_registration_login_gmail(request):
    return TemplateResponse(request,'api/api.html',{})
def customer_forgot_password(request):
    return TemplateResponse(request,'api/api.html',{})
def customer_reset_password(request):
    return TemplateResponse(request,'api/api.html',{})
def customer_bg_image_login_registration(request):
    return TemplateResponse(request,'api/api.html',{})


########## Customer vendor listing detail
def customer_vendor_category_or_home(request):
    return TemplateResponse(request,'api/api.html',{})
def customer_vendor_list_and_search(request):
    return TemplateResponse(request,'api/api.html',{})
def customer_vendor_detail(request):
    return TemplateResponse(request,'api/api.html',{})

########## customer_messages_bid_book_schedule
def customer_mbb_send(request):
    return TemplateResponse(request,'api/api.html',{})
def customer_mbb_list_and_search_and_filter(request):
    return TemplateResponse(request,'api/api.html',{})
def customer_schedule_visit(request):
    return TemplateResponse(request,'api/api.html',{})
def customer_create_bid(request):
    return TemplateResponse(request,'api/api.html',{})
def customer_create_book(request):
    return TemplateResponse(request,'api/api.html',{})


########## vendor_login_registration
def vendor_lead(request):
    return TemplateResponse(request,'api/api.html',{})
def vendor_login(request):
    return TemplateResponse(request,'api/api.html',{})
def vendor_registration_login_fb(request):
    return TemplateResponse(request,'api/api.html',{})
def vendor_registration_login_gmail(request):
    return TemplateResponse(request,'api/api.html',{})
def vendor_forgot_password(request):
    return TemplateResponse(request,'api/api.html',{})
def vendor_reset_password(request):
    return TemplateResponse(request,'api/api.html',{})

########## vendor_calendar_screens
def vendor_calendar_home(request):
    return TemplateResponse(request,'api/api.html',{})
def vendor_calendar_rates_availability(request):
    return TemplateResponse(request,'api/api.html',{})

########## 
def vendor_messages_bid_book(request):
    return TemplateResponse(request,'api/api.html',{})
def vendor_mbb_send(request):
    return TemplateResponse(request,'api/api.html',{})
def vendor_mbb_list_and_search_and_filter(request):
    return TemplateResponse(request,'api/api.html',{})
def vendor_respond_bid(request):
    return TemplateResponse(request,'api/api.html',{})
def vendor_respond_book(request):
    return TemplateResponse(request,'api/api.html',{})
