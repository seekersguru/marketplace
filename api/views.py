from django.template.response import TemplateResponse
from api.urls import patterns
from django.views.decorators.csrf import csrf_exempt
from collections import OrderedDict
from utils import response

from api.utils import get_error as ge , get_success as gs
import utils
from customer.models import Customer
from vendor.models import Category, VendorLead, Vendor
from wedwise_messages.models import Messages
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
                  error_fields=req_missing)    

    #return TemplateResponse(request,'api/api.html',{"res":res})

def index(request):
    lst=[ (k,v) for k,v in patterns.iteritems()]
    lst=OrderedDict(sorted(lst, key= lambda e:e[1]['order']))
    return TemplateResponse(request,'api/api_index.html',
                {"patterns":lst})

########## Customer Login Registration
@csrf_exempt
def customer_registration(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("customer_registration",request,"POST")
    if invalid:return response(request,invalid) 
    
    if request.method=="POST":
        return response(request,Customer.create(request))

@csrf_exempt
def vendor_registration(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("vendor_registration",request,"POST")
    if invalid:return response(request,invalid) 
    
    if request.method=="POST":
        return response(request,Vendor.create(request))
    

@csrf_exempt
def customer_login(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("customer_login",request,"POST")
    if invalid:return response(request,invalid)
    if request.method=="POST":
        return response(request,Customer.login(request))
@csrf_exempt
def customer_registration_login_fb_gm(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("customer_registration_login_fb_gm",request,"POST")
    if invalid:return response(request,invalid)
    if request.method=="POST":
        return response(request,Customer.login_fb_gm(request))

def customer_forgot_password(request):
    return TemplateResponse(request,'api/api.html',{})
def customer_reset_password(request):
    return TemplateResponse(request,'api/api.html',{})



########## Customer vendor listing detail
@csrf_exempt
def customer_vendor_category_or_home(request):
        #TODO Put all in decorators  with csrf 
        invalid=check_basic_validations("customer_vendor_category_or_home",request,"POST")
        if invalid:return response(request,invalid) 
        return response(request,Category.get_categories(request))

@csrf_exempt
def customer_bg_image_login_registration(request):
    invalid=check_basic_validations("customer_bg_image_login_registration",request,"POST")
    if invalid:return response(request,invalid)
    return response(request,utils.get_bg_images_login(request))

@csrf_exempt
def customer_vendor_list_and_search(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("customer_vendor_list_and_search",request,"POST")
    if invalid:return response(request,invalid) 
    return response(request,Vendor.get_listing(request))
    
@csrf_exempt
def customer_vendor_detail(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("customer_vendor_detail",request,"POST")
    if invalid:return response(request,invalid) 
    return response(request,Vendor.get_vendor_detail(request))

########## customer_messages_bid_book_schedule
@csrf_exempt
def customer_vendor_message_create(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("customer_vendor_message_create",request,"POST")
    if invalid:return response(request,invalid) 

    return response(request,Messages.create(request))
@csrf_exempt
def customer_vendor_message_detail(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("customer_vendor_message_detail",request,"POST")
    if invalid:return response(request,invalid) 

    return response(request,Messages.details(request))

@csrf_exempt
def customer_vendor_bid_book_detail(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("customer_vendor_bid_book_detail",request,"POST")
    if invalid:return response(request,invalid) 

    return response(request,Messages.vendor_bid_book_page(request))

@csrf_exempt
def customer_vendor_message_list(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("customer_vendor_message_list",request,"POST")
    if invalid:return response(request,invalid) 

    return response(request,Messages.listing(request))

def customer_schedule_visit(request):
    return TemplateResponse(request,'api/api.html',{})
def customer_create_bid(request):
    return TemplateResponse(request,'api/api.html',{})
def customer_create_book(request):
    return TemplateResponse(request,'api/api.html',{})


########## vendor_login_registration
# @csrf_exempt
# def vendor_lead(request):
#     #TODO Put all in decorators  with csrf 
#     invalid=check_basic_validations("vendor_lead",request,"POST")
#     if invalid:return response(request,invalid) 
# 
#     if request.method=="POST":
#         return response(request,VendorLead.create(request))
## TODO Remove all vendor_lead stuff

@csrf_exempt
def vendor_login(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("vendor_login",request,"POST")
    if invalid:return response(request,invalid)
    if request.method=="POST":
        return response(request,Vendor.login(request))
@csrf_exempt
def vendor_registration_login_fb_gm(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("vendor_registration_login_fb_gm",request,"POST")
    if invalid:return response(request,invalid)
    if request.method=="POST":
        return response(request,Vendor.login_fb_gm(request))

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

