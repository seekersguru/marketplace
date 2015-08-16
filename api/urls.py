from django.conf.urls import url
from collections import OrderedDict
from utils import ALLOWED_ANDRIOD_IMAGE_TYPE,ALLOWED_IOS_IMAGE_TYPE
from wedwise_messages.models import FROM_TO_CHOICES
urlpatterns = [
	## Home page for apis 
    url(r'^$','api.views.index', name='api_index'),
]
from vendor.models import Vendor
from customer.models import Customer
vendor_identfiers=[ [e.identifier,e.identifier ] for e in Vendor.active_object.all()]
customer_identfiers=[[e.identifier,e.identifier ] for e in Customer.objects.all()]
vendor_identfiers.extend(customer_identfiers)
identifiers=vendor_identfiers
vendor_emails=[ [e.user.username,e.user.username, ] for e in Vendor.active_object.all()]
from wedwise_messages.models import MESSAGE_TYPES_CHOICES
from vendor.models import VENDOR_TYPES
patterns = {##"customer_login_registration",


	
		"customer_registration":
	 		{
				"type":"POST",
				"order":1,
	 			"params":["email","password","groom_name","bride_name","contact_number","fbid","gid","identifier","operation",
						"tentative_wedding_date","contact_name"],
	 			"required_params":["email","password","groom_name","bride_name","contact_number","contact_name"],
	 			"help":{"operation":"get or update","identifier":"When get or update"},
	 			
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
	 			"params":["email",	],
	 			"required_params":["email",	]
		 	}, 
		 	
# 		"customer_reset_password":
# 			{
# 				"type":"POST",
# 				"order":6,
# 	 			"params":["email","code","password","confirm_password"],
# 	 			"required_params":["email","code","password","confirm_password"],
# 	 			
# 		 	},
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
	 			"params":["mode","image_type","vendor_type","page_no","search_string","favorites","identifier"],
	 			"required_params":["mode","image_type"],
	 			"help":{"mode":"Possible values 'android' or 'ios'",
						"image_type":"For android allowed: " + str(ALLOWED_ANDRIOD_IMAGE_TYPE)\
						+ "<br/>For ios allowed :"+str(ALLOWED_IOS_IMAGE_TYPE)}, 
	 			# Better pick from DB
	 			"selects":{"vendor_type":VENDOR_TYPES}

		 	},
		"add_favorite":
	 		{
				"type":"POST",
				"order":8,
	 			"params":["identifier","vendor_email","favorite"],
	 			"required_params":["identifier","vendor_email","favorite"],
	 			"selects":{"favorite":[["1","1"],["-1","-1"]],"identifier":identifiers},
	 			"help":{"identifier":"Should be customer"}, 


		 	},
		"customer_vendor_detail":
		 	{
				"type":"POST",
				"order":-20,
	 			"params":["mode","image_type","vendor_email","identifier"],
	 			"required_params":["mode","image_type","vendor_email"],
	 			"selects":{"vendor_email": vendor_emails,"identifier":identifiers},
	 			"help":{"mode":"Possible values 'android' or 'ios'",
						"image_type":"For android allowed: " + str(ALLOWED_ANDRIOD_IMAGE_TYPE)\
						+ "<br/>For ios allowed :"+str(ALLOWED_IOS_IMAGE_TYPE),
						"vendor_email":"https://docs.google.com/document/d/1YU3aJUd4bAb13LfFMMHEGMpS8lCt3utSZE6IEu1K23I/edit?usp=sharing"
						}, 
				
		 	},
	

		"schedule_visit":
			{
				"order":-1111,
				"type":"POST",
	 			"params":[
							"vendor_email","identifier","time",
						],
	 			"required_params":["vendor_email","identifier","time",],
	 			"selects":{"identifier":identifiers},
	 			"help":{"time":"yyyy-mm-dd hh:mm"}
		 	},	
		"locations": 
			{
				"order":-1111,
				"type":"POST",
	 			"params":["match_string"],
	 			"required_params":[],
		 	},	
		"check_availability": 
			{
				"order":-1111,
				"type":"POST",
	 			"params":[
							"vendor_email","identifier","time_slot","event_date"
						],
	 			"required_params":["vendor_email","identifier","time_slot","event_date"],
	 			"selects":{"identifier":identifiers},
	 			"help":{"time":"yyyy-mm-dd hh:mm"}
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
	 			"selects":{"from_to": FROM_TO_CHOICES,"msg_type":MESSAGE_TYPES_CHOICES,"identifier":identifiers},
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
	 			"selects":{"from_to": FROM_TO_CHOICES,"msg_type":MESSAGE_TYPES_CHOICES ,"identifier":identifiers }
		 	},
		##"customer_messages_bid_book_schedule",
		"customer_vendor_message_list":
			{
				"order":-9,
				"type":"POST",
	 			"params":["identifier","page_no","from_to","msg_type"],#["identifier"]
	 			"required_params":["identifier","from_to","msg_type"],
	 			"selects":{"from_to": FROM_TO_CHOICES,"msg_type":MESSAGE_TYPES_CHOICES,"identifier":identifiers }
		 	},
	 	
	 	"customer_schedule_visit":
	 		{
				"order":13,
				"type":"POST",
	 			"params":[]
		 	},
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
	 			"params":["email",	],
	 			"required_params":["email",	]
		 	}, 
		 	
# 		"vendor_reset_password":
# 			{
# 				"type":"POST",
# 				"order":6,
# 	 			"params":["email","code","password","confirm_password"],
# 	 			"required_params":["email","code","password","confirm_password"],
# 	 			
# 		 	},

	##"vendor_calendar_screens",
	
	 	"vendor_calendar_home":
	 		{
				"order":-222,
				"type":"POST",
	 			"params":["year","month","filter_string","identifier"],
	 			"required_params":["identifier"],
	 			"selects":{"identifier":identifiers },
	 			"help":{"filter_string":"k1=v1&k2=v21,v22,v23&k3=v3  | date='yyyy-mm-dd'"}
		 	},
	 	"vendor_calendar_availability":
	 		{
				"order":-222,
				"type":"POST",
	 			"params":["year","month","time_slot","avail_type","identifier","dates","mode","image_type"],
	 			"required_params":["year","month","identifier",],#"mode","image_type"],
	 			"selects":{"identifier":identifiers },
	 			"help":{"time_slot":"morning | evening | all_day",
						"avail_type":"available (green) | ongoing_enquiry (orange) | booked (red)",
						"dates":"yyyy-mm-dd,yyyy-mm-dd,yyyy-mm-dd",
						"mode":"Possible values 'android' or 'ios'",
						"image_type":"For android allowed: " + str(ALLOWED_ANDRIOD_IMAGE_TYPE)\
						+ "<br/>For ios allowed :"+str(ALLOWED_IOS_IMAGE_TYPE)
						}
		 	},



# 		
# 		"vendor_calendar_rates_availability":
# 			{
# 				"order":-223,
# 				"type":"POST",
# 	 			"params":["year","month","packages","dates"],
# 		 	}, 
		"vendor_bid_book_detail":
			{
				"order":-110,
				"type":"POST",
	 			"params":["identifier","msg_id","msg_type",],
	 			"required_params":["identifier","msg_id","msg_type"],
	 			"selects":{"msg_type":[["bid","Bid"]] ,"identifier":identifiers }
		 	},	
		"vendor_bid_book_response":
			{
				"order":-110,
				"type":"POST",
	 			"params":["identifier","msg_id","status",],
	 			"required_params":["identifier","msg_id","status",],
	 			"selects":{"identifier":identifiers}
	 			
		 	},	

	} 
	
	



urlpatterns += [url(r'^%s/'%pattern , 'api.views.%s'%pattern , name='%s'%pattern) for pattern in patterns]

