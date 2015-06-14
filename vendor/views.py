from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from vendor.vendor_rules import banquet_rule
#import static url form setting
from market_place.settings import STATIC_URL
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



@csrf_exempt
def banquets(request):
    banquet_rule_copy=banquet_rule[:]
    if request.method =="POST":
        banquet_rule_copy=vendor_validation(request, banquet_rule_copy)
    
    
    return TemplateResponse (request,'banquets.html',
                             {"rules":banquet_rule_copy ,
                             "message":"Some Message on the top ",
                             "message_class":"",
                             'static_url' : STATIC_URL
                            }
                             )
