from django.conf.urls import url
from collections import OrderedDict
urlpatterns = [
	## Home page for apis 
    url(r'^$','api.views.index', name='api_index'),
]
patterns =\
[
	##"customer_login_registration",
	"customer_registration",
	"customer_login",
	"customer_registration_login_fb",
	"customer_registration_login_gmail", 
	"customer_forgot_password", 
	"customer_reset_password",
	#Make it simple some how. according to version replace existing default 
	##and add new some how
	"customer_bg_image_login_registration" ,
	
	##"customer_vendor_listing_detail",
	
	"customer_vendor_category_or_home",
	"customer_vendor_list_and_search",
	"customer_vendor_detail",
	

	##"customer_messages_bid_book_schedule",
	
	"customer_mbb_send",
	"customer_mbb_list_and_search_and_filter",
	"customer_schedule_visit",
	"customer_create_bid",
	"customer_create_book",
	

	##"vendor_login_registration",
	
	"vendor_lead",
	"vendor_login",
	"vendor_registration_login_fb",
	"vendor_registration_login_gmail", 
	"vendor_forgot_password", 
	"vendor_reset_password", 

	##"vendor_calendar_screens",
	
	"vendor_calendar_home",
	"vendor_calendar_rates_availability", 

	#"vendor_messages_bid_book",
	
	"vendor_mbb_send",
	"vendor_mbb_list_and_search_and_filter",
	"vendor_respond_bid",
	"vendor_respond_book", 
	
	
]


urlpatterns += [url(r'^%s/'%pattern , 'api.views.%s'%pattern , name='%s'%pattern) for pattern in patterns]

