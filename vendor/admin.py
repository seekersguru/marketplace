from django.contrib import admin
from django.contrib.auth.models import User
from models import Category, Vendor

  

    
class VendorAdmin(admin.ModelAdmin):
    model = Vendor

 
    

admin.site.register(Vendor, VendorAdmin)
