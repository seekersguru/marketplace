from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.

from vendor.vendor_rules import banquet_rule
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def banquets(request):
    
    return TemplateResponse (request,'banquets.html',
                             {"rules":banquet_rule ,
                             "message":"Some Message on the top ",
                             "message_class":""
                            }
                             )
