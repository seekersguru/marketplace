from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http.response import HttpResponseRedirect
from market_place.settings import MEDIA_PATH

def clear_console(request,vendor_id=None):
    f=open(MEDIA_PATH.replace("media","templates/console.html"),"w")
    f.write("""<a href ="/clear_console/"> Clear Console </a> <br/><br/><br/>""")
    f.close()
    return HttpResponseRedirect("/console/")
    

# Create your views here.
def vendor_page(request,vendor_id=None): 
    return TemplateResponse(request, "web/vendor_page.html",
                            {"top_header_title" :"Vendor Data",
                             "page_title":"Vendor Form",
                             "info_section_heading":"Vendor Data",
                             "info_section_sub_heading":"To insert Vendor data."
                                
                             }
                            )
# Create your views here.
def index(request):
    return TemplateResponse(request, "web/index.html",
                            {"top_header_title" :"Home",
                             "page_title":"Web Home",
                             "info_section_heading":"Welcome to wedwise",
                             "info_section_sub_heading":"Wedding arangements are fun!"
                             }
                            )

# Create your views here.
def home(request):    
    return TemplateResponse(request, "web/home.html",
                            {"user" :request.user,
                             "top_header_title" :"Welcome "+str(request.user.customer.contact_name),
                             "page_title":"Welcome "+str(request.user.customer.contact_name),
                             "info_section_heading":"Welcome to wedwise",
                             "info_section_sub_heading":"Wedding arangements are fun!"
                             }
                            )