from django.contrib import admin
from django.contrib.auth.models import User
from models import Category, Vendor, VendorUser, VendorField, Fields


class UserInlineAdmin(admin.StackedInline):
    model = VendorUser
    extra=1    

    
class VendorAdmin(admin.ModelAdmin):
    fields = ['category', 'name', 'contact_number', 'address', 'email']
    model = Vendor

    inlines = [UserInlineAdmin]
    
# Register your models here.
admin.site.register(Category)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(VendorUser)
admin.site.register(VendorField)
admin.site.register(Fields)
