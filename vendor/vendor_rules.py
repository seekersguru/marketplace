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

banquet_rule=\
{
    "basic_info":{
        LABEL:"Basic Info",
        FIELDS:[
                widget_input("Name","name",True,2,50),
                widget_input("Address","address",True,2,50),
               
        ]
     
    }

}




for section_name,section_info  in banquet_rule.iteritems():
    print section_name , section_info[LABEL]
    for field in section_info[FIELDS]:
        print field