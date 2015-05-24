# core/api.py
from tastypie.authorization import DjangoAuthorization, Authorization
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.http import HttpUnauthorized, HttpForbidden
from tastypie.utils import trailing_slash

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.conf.urls import url
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

    def override_urls(self):
            return [
                url(r"^(?P<resource_name>%s)/login%s$" %
                    (self._meta.resource_name, trailing_slash()),
                    self.wrap_view('login'), name="api_login"),
                url(r'^(?P<resource_name>%s)/logout%s$' %
                    (self._meta.resource_name, trailing_slash()),
                    self.wrap_view('logout'), name='api_logout'),
            ]

    def login(self, request, **kwargs):
        self.method_check(request, allowed=['post'])

        data = self.deserialize(request, request.raw_post_data, format=request.META.get('CONTENT_TYPE', 'application/json'))

        username = data.get('username', '')
        password = data.get('password', '')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return self.create_response(request, {
                    'success': True
                })
            else:
                return self.create_response(request, {
                    'success': False,
                    'reason': 'disabled',
                    }, HttpForbidden )
        else:
            return self.create_response(request, {
                'success': False,
                'reason': 'incorrect',
                }, HttpUnauthorized )

    def logout(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        if request.user and request.user.is_authenticated():
            logout(request)
            return self.create_response(request, { 'success': True })
        else:
            return self.create_response(request, { 'success': False }, HttpUnauthorized)
                
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
        
        