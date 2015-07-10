from django.conf.urls import url
from collections import OrderedDict
from utils import ALLOWED_ANDRIOD_IMAGE_TYPE,ALLOWED_IOS_IMAGE_TYPE
from wedwise_messages.models import FROM_TO_CHOICES
urlpatterns = [
	## Home page for apis 
    url(r'^$','api.views.index', name='api_index'),
]
from wedwise_messages.models import MESSAGE_TYPES_CHOICES
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
				"order":-20,
	 			"params":["mode","image_type","vendor_email"],
	 			"required_params":["mode","image_type","vendor_email"],
	 			"help":{"mode":"Possible values 'android' or 'ios'",
						"image_type":"For android allowed: " + str(ALLOWED_ANDRIOD_IMAGE_TYPE)\
						+ "<br/>For ios allowed :"+str(ALLOWED_IOS_IMAGE_TYPE),
						"vendor_email":"https://docs.google.com/document/d/1YU3aJUd4bAb13LfFMMHEGMpS8lCt3utSZE6IEu1K23I/edit?usp=sharing"
						}, 
		 	},
	
	 			
	 					
		"customer_vendor_message_create":
			{
				"order":-11,
				"type":"POST",
	 			"params":[
							"mode","device_id","push_data","identifier","receiver_email","message","from_to",
							"msg_type","bid_json","book_json","event_date","time_slot",
							"bid_price","bid_quantity"
						],
	 			"required_params":["device_id","push_data","identifier","receiver_email","message","from_to"],
	 			"selects":{"from_to": FROM_TO_CHOICES,"msg_type":MESSAGE_TYPES_CHOICES},
	 			"help":{
						"fom_to":"(Also not for bid and book only c2v.)",
						"mode":"Possible values 'android' or 'ios'",
						"device_id":"Id of the device.",
						"push_data":"Data to be pushed as notification and parsed on other client's side",
						"bid_json":"'bid' value from vendor detail page, used to render bid page",
						"event_date":"required for bid/book and format is yyyy-mm-dd",
						"book_json":"'book' value from vendor detail page, used to render book page",
						"bid_price":"(float value) Required in bid",
						"bid_quantity":"(int value) Optional in bid, if provided from vendor detail json",
						"time_slot":"required in bid and book and must be from one of the values from 'time_slot' from vendor detail response"
						},
	 			 
		 	},
		"customer_vendor_message_detail":
			{
				"order":-10,
				"type":"POST",
	 			"params":["identifier","receiver_email","page_no","from_to","msg_type"],
	 			"required_params":["identifier","receiver_email","from_to","msg_type"],
	 			"selects":{"from_to": FROM_TO_CHOICES,"msg_type":MESSAGE_TYPES_CHOICES  }
		 	},
		"customer_vendor_bid_book_detail":
			{
				"order":-110,
				"type":"POST",
	 			"params":["identifier","msg_id","msg_type"],
	 			"required_params":["identifier","msg_id","msg_type"],
	 			"selects":{"msg_type":[["bid","Bid"],["book","Book"]]  }
		 	},	
		##"customer_messages_bid_book_schedule",
		"customer_vendor_message_list":
			{
				"order":-9,
				"type":"POST",
	 			"params":["identifier","page_no","from_to","msg_type"],#["identifier"]
	 			"required_params":["identifier","from_to","msg_type"],
	 			"selects":{"from_to": FROM_TO_CHOICES,"msg_type":MESSAGE_TYPES_CHOICES }
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

