validation_rules={
                  "integer": lambda x : x.isdigit()
                  
                  
                  }


LABEL="label"
FIELDS ="fields"
NAME = "name"
REQUIRED= "required"
MIN_LENGTH="min_length"
MAX_LENGTH= "max_length"
TYPE = "type"
VALIDATIONS = "validations"
HELP_TEXT="help_text"
CHOICES="choices"
YES_NO_CHOICES=[(-1,"---"),(0,"Yes"),(1,"No")]
FOOD_TYPE_CHOICES =(
                    ("veg","Veg"),
                    ("non_veg","Non-Veg"),
                    ("jain_only","Jain only"),
                    ("alcohol","Alcohol"),
                    )
VENUE_TYPE_CHOICES =(
                    ("hotel","Hotel"),
                    ("banquette hall","Banquette Hall"),
                    ("party lawn","Party Lawn"),
                    ("farmhouse","Farm House"),
                    )
SELECT_TYPE, CHECKBOX_TYPE, RADIO_TYPE="select","checkbox","radio"
def widget_input(label,name,required,min_len , max_len 
                 ,validations=[],
                 help_text=""):
    return  {   
                LABEL : label,
                NAME:name,
                REQUIRED:required,
                MIN_LENGTH:min_len,
                MAX_LENGTH:max_len,
                TYPE:"input",
                VALIDATIONS:validations, 
                HELP_TEXT:help_text
            }
def widget_choice(label,name,required  
                 ,validations=[],
                 help_text="",choices=[],
                 widget_type=SELECT_TYPE# CHECKBOX_TYPE | RADIO_TYPE
                 ):
    return  {   
                LABEL : label,
                NAME:name,
                REQUIRED:required,
                TYPE:widget_type,
                VALIDATIONS:validations, 
                HELP_TEXT:help_text,
                CHOICES:choices
            }
from collections import OrderedDict
banquet_rule=\
[{
        LABEL:"Basic Info",
        FIELDS:[
                widget_input("Name","name",True,2,50,[],"Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only."),
                widget_input("Address","address",True,2,70),
                widget_input("Phone","phone",True,2,12),
                widget_input("Neighbouhood","neighbouhood",True,2,50),
                widget_input("GPS Co_Ordinates","gps co_ordinates",True,2,50),
                widget_input("Capacity_floating","capacity_floating",True,2,800),
                widget_choice("Food Type","food_type",True,choices=FOOD_TYPE_CHOICES,
                              widget_type=CHECKBOX_TYPE),
                widget_choice("Parking_spot","parkingspot",True,choices=FOOD_TYPE_CHOICES,
                              widget_type=CHECKBOX_TYPE),
        ]
    },


    {
        LABEL:"Pricing",
        FIELDS:[
                widget_input("Billing","billing",True,2,50,[],"Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only."),
                widget_input("Hallrental","hallrental",True,2,70),
               
        ]
    },
    
    {
        LABEL:"facilites",
        FIELDS:[
                widget_choice("Venue_Type","venuetype",True,choices=VENUE_TYPE_CHOICES,
                              widget_type=CHECKBOX_TYPE),
                widget_choice("Ac","ac",True,choices=YES_NO_CHOICES, widget_type=SELECT_TYPE),
                widget_choice("PowerBackup","powerbackup",True,choices=YES_NO_CHOICES, widget_type=SELECT_TYPE),
                widget_choice("Restrooms","restrooms",True,choices=YES_NO_CHOICES, widget_type=SELECT_TYPE),
                widget_choice("Shower","shower",True,choices=YES_NO_CHOICES, widget_type=SELECT_TYPE),
                widget_choice("BridalRoom","bridalroom",True,choices=YES_NO_CHOICES, widget_type=SELECT_TYPE),
                widget_choice("Elevator","elevator",True,choices=YES_NO_CHOICES, widget_type=SELECT_TYPE),
                widget_choice("Ramp","Ramp",True,choices=YES_NO_CHOICES, widget_type=SELECT_TYPE),
                widget_choice("Wheelchairs","wheelchairs",True,choices=YES_NO_CHOICES, widget_type=SELECT_TYPE),
                widget_choice("Chairs","chairs",True,choices=YES_NO_CHOICES, widget_type=SELECT_TYPE),
                widget_choice("Chaircovers","chaiecovers",True,choices=YES_NO_CHOICES, widget_type=SELECT_TYPE),
                widget_choice("Tables","tables",True,choices=YES_NO_CHOICES, widget_type=SELECT_TYPE),
                widget_choice("Tablecovers","tablecovers",True,choices=YES_NO_CHOICES, widget_type=SELECT_TYPE),
                widget_choice("Poolside","poolside",True,choices=YES_NO_CHOICES, widget_type=SELECT_TYPE),
                widget_choice("OvermightRoom","overmightroom",True,choices=YES_NO_CHOICES, widget_type=SELECT_TYPE),
                
                
                
        ]
     }
]





# for section_name,section_info  in banquet_rule.iteritems():
#     print section_name , section_info[LABEL]
#     for field in section_info[FIELDS]:
#         print field