from django.conf.urls import url
from collections import OrderedDict
from utils import ALLOWED_ANDRIOD_IMAGE_TYPE,ALLOWED_IOS_IMAGE_TYPE
from wedwise_messages.models import FROM_TO_CHOICES
urlpatterns = [
	## Home page for apis 
    url(r'^$','api.views.index', name='api_index'),
]
from vendor.models import VENDOR_TYPES
patterns = {##"customer_login_registration",
	
		"customer_registration":
	 		{
				"type":"POST",
				"order":1,
	 			"params":["email","password","groom_name","bride_name","contact_number","fbid","gid"],
	 			"required_params":["email","password","groom_name","bride_name","contact_number"]
		 	},
		"customer_login":
			{
			"type":"POST",
			"order":2,
			"params":["email","password",],
			"required_params":["email","password",]
			},
	
		"customer_registration_login_fb_gm":
			{
				"type":"POST",
				"order":3,
		 		"params":["email"],
		 		"required_params":["email",	]
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
	 			"params":["mode","image_type"],
	 			"required_params":["mode","image_type"],
	 			"help":{"mode":"Possible values 'android' or 'ios'",
						"image_type":"For android allowed: " + str(ALLOWED_ANDRIOD_IMAGE_TYPE)\
						+ "<br/>For ios allowed :"+str(ALLOWED_IOS_IMAGE_TYPE)}
		 	},
	
	##"customer_vendor_listing_detail","type":"POST",

	 	"customer_vendor_category_or_home":
	 		{
				"type":"POST",
				"order":8,
	 			"params":["mode","image_type"],
	 			"required_params":["mode","image_type"],
	 			"help":{"mode":"Possible values 'android' or 'ios'",
						"image_type":"For android allowed: " + str(ALLOWED_ANDRIOD_IMAGE_TYPE)\
						+ "<br/>For ios allowed :"+str(ALLOWED_IOS_IMAGE_TYPE)}
		 	},
		 
		"customer_vendor_list_and_search":
	 		{
				"type":"POST",
				"order":8,
	 			"params":["mode","image_type","vendor_type","page_no","search_string"],
	 			"required_params":["mode","image_type","vendor_type"],
	 			"help":{"mode":"Possible values 'android' or 'ios'",
						"image_type":"For android allowed: " + str(ALLOWED_ANDRIOD_IMAGE_TYPE)\
						+ "<br/>For ios allowed :"+str(ALLOWED_IOS_IMAGE_TYPE)}, 
	 			# Better pick from DB
	 			"selects":{"vendor_type":VENDOR_TYPES}

		 	},
		"customer_vendor_detail":
		 	{
				"type":"POST",
				"order":10,
	 			"params":[]
		 	},
	

		"customer_message_create":
			{
				"order":-11,
				"type":"POST",
	 			"params":["identifier","receiver_email","message","from_to"],
	 			"required_params":["identifier","receiver_email","message","from_to"],
	 			"selects":{"from_to": FROM_TO_CHOICES }
		 	},
		"customer_message_detail":
			{
				"order":-10,
				"type":"POST",
	 			"params":["identifier","vendor_email","page_no"],
	 			"required_params":["identifier","vendor_email"],
		 	},
	
		##"customer_messages_bid_book_schedule",
		"customer_message_list":
			{
				"order":-9,
				"type":"POST",
	 			"params":["identifier","page_no"],#["identifier"]
	 			"required_params":["identifier",]
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
	
# 	 	"vendor_lead":
# 			{
# 				"order":18,
# 				"type":"POST",
# 	 			"params":["email","name","mobile","address","services","fbid","gid"],
# 	 			"required_params":["email","name","mobile","address","services"],
# 		 	},
		"vendor_registration":
	 		{#In last so can add categories and dump the json for corresponding category

				"type":"POST",
				"order":155,
	 			"params":["email" ,"password" ,"vendor_type" ,"name","contact_number","address","fbid","gid"],
	 			"required_params":["email" ,"password" ,"vendor_type" ,"name","contact_number","address"],
	 			# Better pick from DB
	 			"selects":{"vendor_type":VENDOR_TYPES}
		 	},
		"vendor_login":
			{
			"type":"POST",
			"order":17,
			"params":["email","password",],
			"required_params":["email","password",]
			},
		 

		"vendor_registration_login_fb_gm":
			{
				"type":"POST",
				"order":18,
		 		"params":["email"],
		 		"required_params":["email",	]
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

