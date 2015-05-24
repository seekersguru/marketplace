# core/api.py
from tastypie.authorization import DjangoAuthorization, Authorization
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

from django.contrib.auth.models import User
from django.db import IntegrityError
from core.models import Category, Vendor, UserMember, VendorField, Fields


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()

        filtering = {
            'name': ALL,
        }


class VendorResource(ModelResource):
    class Meta:
        queryset = Vendor.objects.all()
        resource_name = 'vendor'
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()

        filtering = {
            'name': ALL,
        }

class UserResource(ModelResource):
    class Meta:
        object_class = User
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()
        allowed_methods = ['get','post', 'delete', 'put']
        
        excludes = ['password', 'is_staff', 'is_superuser']
        filtering = {
            'username': ALL,
        }
        
    def obj_create(self, bundle, **kwargs):
        try:
            bundle = super(UserResource, self).obj_create(bundle, **kwargs)
            bundle.obj.set_password(bundle.data.get('password'))
            bundle.obj.save() 
        except IntegrityError:
            raise BadRequest('That username already exists')
        return bundle        

        
class UserMemberResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    vendor = fields.ForeignKey(VendorResource, 'vendor')
    
    class Meta:
        queryset = UserMember.objects.all()
        resource_name = 'usermember'
        

class FieldsResource(ModelResource):
    class Meta:
        queryset = Fields.objects.all()
        resource_name = 'fields'
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()

        filtering = {
            'name': ALL,
        }
        
        
class VendorFieldResource(ModelResource):
    user = fields.ForeignKey(FieldsResource, 'fields')
    vendor = fields.ForeignKey(VendorResource, 'vendor')

    class Meta:
        queryset = VendorField.objects.all()
        resource_name = 'vendorfield'
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()

        filtering = {
            'vendor__name': ALL,
        }
        
        