from django.contrib import admin
from models import Category, Vendor, UserMember, VendorField, Fields


# Register your models here.
admin.site.register(Category)
admin.site.register(Vendor)
admin.site.register(UserMember)
admin.site.register(VendorField)
admin.site.register(Fields)
