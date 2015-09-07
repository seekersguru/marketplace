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
def index(request,vendor_id=None):
    return TemplateResponse(request, "web/index.html",{"name" "nishant ",})

