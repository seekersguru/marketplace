from django.conf.urls import url
from collections import OrderedDict
urlpatterns = [
	## Home page for apis 
    url(r'^$','api.views.index', name='api_index'),
]

patterns = {##"customer_login_registration",
	
		"customer_registration":
	 		{
				"type":"POST",
				"order":1,
	 			"params":["email","password","groom_name","bride_name","contact_number"],
	 			"required_params":["email","password","groom_name","bride_name","contact_number"]
		 	},
		"customer_login":
			{
			"type":"POST",
			"order":2,
				"params":[]
			},
	
		"customer_registration_login_fb":
			{
				"type":"POST",
				"order":3,
		 		"params":[]
			 },

		"customer_registration_login_gmail":
			{
				"type":"POST",
				"order":4,
		 		"params":[]
			}, 

	 	"customer_forgot_password":
	 		{
				"type":"POST",
				"order":5,
	 			"params":[]
		 	}, 
		 	
		"customer_reset_password":
			{
				"type":"POST",
				"order":6,
	 			"params":[]
		 	},
	#Make it simple some how. according to version replace existing default 
	##and add new some how
		"customer_bg_image_login_registration" :
			{
				"type":"POST",
				"order":7,
	 			"params":[]
		 	},
	
	##"customer_vendor_listing_detail","type":"POST",

	 	"customer_vendor_category_or_home":
	 		{
				"type":"POST",
				"order":8,
	 			"params":[]
		 	},
		 
		"customer_vendor_list_and_search":
			{
				"type":"POST",
				"order":9,
	 			"params":[]
		 	},
		"customer_vendor_detail":
		 	{
				"type":"POST",
				"order":10,
	 			"params":[]
		 	},
	

		##"customer_messages_bid_book_schedule",
		"customer_mbb_send":
			{
				"order":11,
				"type":"POST",
	 			"params":[]
		 	},
		"customer_mbb_list_and_search_and_filter":
			{
				"order":12,
				"type":"POST",
	 			"params":[]
		 	},
	
	 	"customer_schedule_visit":
	 		{
				"order":13,
				"type":"POST",
	 			"params":[]
		 	},
		 
		"customer_create_bid":
			{
				"order":14,
				"type":"POST",
	 			"params":[]
		 	},
		 
		"customer_create_book":
			{
				"order":15,
				"type":"POST",
	 			"params":[]
		 	},
	

	##"vendor_login_registration",
	
	 	"vendor_lead":
	 		{
				"order":16,
				"type":"POST",
	 			"params":[]
		 	},
		"vendor_login":
			{
				"order":17,
				"type":"POST",
	 			"params":[]
		 	},
		 
		"vendor_registration_login_fb":
			{
				"order":18,
				"type":"POST",
	 			"params":[]
		 	},
		
		"vendor_registration_login_gmail":
			{
				"order":19,
				"type":"POST",
	 			"params":[]
		 	}, 
		"vendor_forgot_password":
		 	{
				"order":20,
				"type":"POST",
	 			"params":[]
		 	}, 
		 	
		"vendor_reset_password":
			{
				"order":21,
				"type":"POST",
	 			"params":[]
		 	}, 

	##"vendor_calendar_screens",
	
	 	"vendor_calendar_home":
	 		{
				"order":22,
				"type":"POST",
	 			"params":[]
		 	},
		
		"vendor_calendar_rates_availability":
			{
				"order":23,
				"type":"POST",
	 			"params":[]
		 	}, 

		#"vendor_messages_bid_book",
	
	
	 	"vendor_mbb_send":
	 		{
				"order":24,
				"type":"POST",
	 			"params":[]
		 	},
	
	 	"vendor_mbb_list_and_search_and_filter":
	 		{
				"order":25,
				"type":"POST",
	 			"params":[]
		 	},
		
		"vendor_respond_bid":
			{
			"order":26,
			"type":"POST",
	 		"params":[]
		 	},
	
	 	"vendor_respond_book":
	 		{
				"order":27,
				"type":"POST",
	 			"params":[]
		 	},
	} 
	
	



urlpatterns += [url(r'^%s/'%pattern , 'api.views.%s'%pattern , name='%s'%pattern) for pattern in patterns]

