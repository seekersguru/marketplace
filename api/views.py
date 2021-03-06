from django.template.response import TemplateResponse
from api.urls import patterns
from django.views.decorators.csrf import csrf_exempt
from collections import OrderedDict
from utils import response

from api.utils import get_error as ge , get_success as gs
import utils
from customer.models import Customer, Favorites
from vendor.models import Category, Vendor
from wedwise_messages.models import Messages, Schedulevisit
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
        return ge("POST",data,"Required fields missing",
                  error_fields=req_missing)    

    #return TemplateResponse(request,'api/api.html',{"res":res})

def index(request):
    lst=[ (k,v) for k,v in patterns.iteritems()]
    
    lst=OrderedDict(sorted(lst, key= lambda e:e[1]['order']))
    return TemplateResponse(request,'api/api_index.html',
                {"patterns":lst, "vendors":Vendor.active_object.all(),"customers":Customer.objects.all()})

########## Customer Login Registration
@csrf_exempt
def customer_registration(request):
    #TODO Put all in decorators  with csrf 
    if request.POST.get("operation")!="get":
        invalid=check_basic_validations("customer_registration",request,"POST")
        if invalid:return response(request,invalid) 
    
    if request.method=="POST":
        return response(request,Customer.create(request))
@csrf_exempt
def customer_otp(request):
    #TODO Put all in decorators  with csrf 
    if request.POST.get("operation")!="get":
        invalid=check_basic_validations("customer_otp",request,"POST")
        if invalid:return response(request,invalid) 
    if request.method=="POST":
        return response(request,Customer.customer_otp(request))
        
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

@csrf_exempt
def customer_forgot_password(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("customer_forgot_password",request,"POST")
    if invalid:return response(request,invalid)
    if request.method=="POST":
        return response(request,Customer.forgot_pwd(request))


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
def add_favorite(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("add_favorite",request,"POST")
    if invalid:return response(request,invalid) 
    return response(request,Favorites.change_value(request)) 

    
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
def vendor_bid_book_detail(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("vendor_bid_book_detail",request,"POST")
    if invalid:return response(request,invalid) 

    return response(request,Messages.vendor_bid_book_page(request))

@csrf_exempt
def delete_message(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("delete_message",request,"POST")
    if invalid:return response(request,invalid) 

    return response(request,Messages.delete_message(request))


@csrf_exempt
def vendor_bid_book_response(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("vendor_bid_book_response",request,"POST")
    if invalid:return response(request,invalid) 

    return response(request,Messages.vendor_bid_book_response(request))

@csrf_exempt
def schedule_visit(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("schedule_visit",request,"POST")
    if invalid:return response(request,invalid) 

    return response(request,Schedulevisit.create_update(request))
@csrf_exempt
def schedule_list(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("schedule_list",request,"POST")
    if invalid:return response(request,invalid) 

    return response(request,Schedulevisit.listing(request))    

@csrf_exempt
def check_availability(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("check_availability",request,"POST")
    if invalid:return response(request,invalid) 

    return response(request,Vendor.check_availability(request))

@csrf_exempt
def locations(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("locations",request,"POST")
    if invalid:return response(request,invalid) 

    return response(request,Vendor.locations(request))

@csrf_exempt
def get_locations_version(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("get_locations_version",request,"POST")
    if invalid:return response(request,invalid) 

    return response(request,Vendor.get_locations_version(request))


@csrf_exempt
def customer_vendor_message_list(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("customer_vendor_message_list",request,"POST")
    if invalid:return response(request,invalid) 

    return response(request,Messages.listing(request))

def customer_schedule_visit(request):
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
@csrf_exempt
def vendor_forgot_password(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("vendor_forgot_password",request,"POST")
    if invalid:return response(request,invalid)
    if request.method=="POST":
        return response(request,Vendor.forgot_pwd(request))



@csrf_exempt
def vendor_calendar_home(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("vendor_calendar_home",request,"POST")
    if invalid:return response(request,invalid)
    if request.method=="POST":
        return response(request,Messages.number_bookings(request))
@csrf_exempt
def vendor_calendar_availability(request):
    #TODO Put all in decorators  with csrf 
    invalid=check_basic_validations("vendor_calendar_availability",request,"POST")
    if invalid:return response(request,invalid)
    if request.method=="POST":
        return response(request,Messages.availability(request))


def vendor_calendar_rates_availability(request):
    return TemplateResponse(request,'api/api.html',{})


