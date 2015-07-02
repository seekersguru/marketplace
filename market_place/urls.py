from django.conf.urls import include, url
from django.contrib import admin
from settings import MEDIA_PATH
from django.views.generic import TemplateView

from api import urls as api_urls


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api_urls)),



#Swagger APIS commented for now
#    url(r'^test-api/$', TemplateView.as_view(template_name='index.html')),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
 
    ##Here add url add banquet and point o core.views.oy#
     url(r'^vendors/$','vendor.views.vendors', name='banquets'),
     url(r'^add_vendor/$','vendor.views.add_vendor', name='add_vendor'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': MEDIA_PATH}),
#     url(r'^api/', include(category_resource.urls)),
]

# urlpatterns += patterns(
#         'django.views.static',
#         (r'^media/(?P<path>.*)',
#         'serve',
#         {'document_root': settings.MEDIA_ROOT}), )