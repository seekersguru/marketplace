from django.conf.urls import include, url
from django.contrib import admin
from settings import MEDIA_PATH

from tastypie.api import Api
from core.api import CategoryResource, UserResource, VendorResource, VendorFieldResource, VendorUserResource, FieldsResource
from django.views.generic import TemplateView
from core.views import add_banquet
v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(CategoryResource())
v1_api.register(VendorResource())
v1_api.register(VendorFieldResource())
v1_api.register(VendorUserResource())
v1_api.register(FieldsResource())
# category_resource = CategoryResource()




urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^test-api/$', TemplateView.as_view(template_name='index.html')),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
 
    ##Here add url add banquet and point o core.views.oy#
     url(r'^add_banquet/$',
        'core.views.add_banquet', name='add_banquet'),
               
     url(r'^banquets/$',
        'vendor.views.banquets', name='banquets'),        

    ## Designs = customer registration flow
    url(r'^customer-login-registration/$', TemplateView.as_view(template_name='customer-login-registration.html')),
     
    url(r'^wedwise-apis/$', TemplateView.as_view(template_name='v1/wedwise.json')),
#     url(r'^media/(?P<path>.*)', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': MEDIA_PATH}),
#     url(r'^api/', include(category_resource.urls)),
]

# urlpatterns += patterns(
#         'django.views.static',
#         (r'^media/(?P<path>.*)',
#         'serve',
#         {'document_root': settings.MEDIA_ROOT}), )