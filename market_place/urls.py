from django.conf.urls import include, url
from django.contrib import admin
from settings import MEDIA_PATH
from django.views.generic import TemplateView

from api import urls as api_urls


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api_urls)),


    
    url(r'^console/$', TemplateView.as_view(template_name='console.html')),
#Swagger APIS commented for now
#    url(r'^test-api/$', TemplateView.as_view(template_name='index.html')),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
 
    ##Here add url add banquet and point o core.views.oy#
     url(r'^vendors/$','vendor.views.vendors', name='banquets'),
     
     url(r'^add_vendor/(?P<vendor_id>[0-9]+)/$','vendor.views.add_vendor', name='add_vendor_id'),
    url(r'^add_vendor/$','vendor.views.add_vendor', name='add_vendor'),

    
     url(r'^add_sample/(?P<vendor_id>[0-9]+)/$','vendor.views.add_sample', name='add_sample_id'),
    url(r'^add_sample/$','vendor.views.add_sample', name='add_sample'),
    
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': MEDIA_PATH}),
    
    
    ## Here comes the web views
    url(r'^web/vendor-page/', "web.views.vendor_page",name="web_vendor_page"),
    url(r'^web/', "web.views.index",name="web_index"),
    
    
    
    
    
    ## Here is the console for apis. ## TODO move to Apis
    url(r'^clear_console/', "web.views.clear_console",name="web_clear_console"),
    



]

