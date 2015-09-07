from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.
def index(request,vendor_id=None):
    return TemplateResponse(request, "web/index.html",{"name" "nishant ",})