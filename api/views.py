from django.template.response import TemplateResponse
from urls import patterns
def index(request):
    return TemplateResponse(request,'api/api_index.html',
                {"patterns":patterns})


########## Customer Login Registration
def customer_registration(request):
    print getdoc(globals()[getframeinfo(currentframe()).function])
    return TemplateResponse(request,'api/api.html',{})
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
def customer_registration(request):
    return TemplateResponse(request,'api/api.html',{})
def customer_registration(request):
    return TemplateResponse(request,'api/api.html',{})
def customer_registration(request):
    return TemplateResponse(request,'api/api.html',{})
def customer_registration(request):
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

