from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from vendor.vendor_rules import banquet_rule
#import static url form setting
from market_place.settings import STATIC_URL
from django.utils import timezone
from django.forms import ModelForm
from vendor.models import Vendor
from utils import get_vendor_meta
class VendorForm(ModelForm):
    class Meta:
        model = Vendor
def vendor_validation(request,vendor_rule):
    request_post=dict(request.POST)
        ## TOD : What the ... , why we need to import to avoid 
        
    vendor_rule_copy = vendor_rule[:]
    
    for index in range(len(vendor_rule)):
        section=vendor_rule[index]
        for index_field in range(len(section["fields"])):
            field =section["fields"][index_field]
            field_name = field["name"]
            
            ### Handling input box 
            if vendor_rule_copy[index]["fields"][index_field]["type"]=="input":
                vendor_rule_copy[index]["fields"][index_field]["value"]=str(request_post.get(field_name)[0])
            
                if vendor_rule_copy[index]["fields"][index_field]["required"] \
                     and (not request_post.get(field_name)[0].strip()):
                        vendor_rule_copy[index]["fields"][index_field]["error"]=1
                else:
                    vendor_rule_copy[index]["fields"][index_field]["error"]=0
     
              
    return vendor_rule_copy 


 
def add_vendor(request):
    message=""
    

    if request.method == "POST":
        form = VendorForm(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            message="Saved succesfully"
    else:
        form = VendorForm()
    
    identifiers = [(e.identifier ,e.user.email) for e in Vendor.objects.all() ]
    return render(request, "add_vendor.html", {'form': form,"message":message
                                               ,"vendors":Vendor.objects.all(),
                                               "vendor_meta":get_vendor_meta() ,
                                               "identifiers":identifiers
                                               })

@csrf_exempt
def vendors(request):
    banquet_rule_copy=banquet_rule[:]
    if request.method =="POST":
        banquet_rule_copy=vendor_validation(request, banquet_rule_copy)
    

    add_vendor_form = VendorForm()

    
    return TemplateResponse (request,'vendors.html',
                             {"rules":banquet_rule_copy ,
                             "message":"Some Message on the top ",
                             "message_class":"",
                             'static_url' : STATIC_URL,
                             "add_vendor_form":add_vendor_form
                            }
                             )
