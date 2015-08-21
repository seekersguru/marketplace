from django.contrib import admin
from django.contrib.auth.models import User
from models import Category, Vendor

  

    
class VendorAdmin(admin.ModelAdmin):
    fields = ('vendor_type', 'user', 'name', 'dynamic_info', 'availability',)
    model = Vendor
    list_display = ('vendor_type','name','active')
    #readonly_fields=('vendor_type', 'user', 'name', 'dynamic_info', 'availability',)
    list_filter = ('active','vendor_type')
class CategoryAdmin(admin.ModelAdmin):
    model = Category 
    

admin.site.register(Vendor, VendorAdmin)
admin.site.register(Category, CategoryAdmin)
