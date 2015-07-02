ALLOWED_ANDRIOD_IMAGE_TYPE=["drawable-hdpi", "drawable-xhdpi", "drawable-xxhdpi","drawable-xxxhdpi",]
ALLOWED_IOS_IMAGE_TYPE=["2x", "3x",]
from utils import ALLOWED_ANDRIOD_IMAGE_TYPE,ALLOWED_IOS_IMAGE_TYPE
LOGIN_IMAGES=["logreg1","logreg2",]

import json
from django.http import HttpResponse

def response(request,res):
    return  HttpResponse(json.dumps(res), content_type="application/json")



def get_bg_images_login(request):
    required_mode=mode_require(request)
    if  "error" in required_mode: return required_mode["error"]
    else:
        mode= required_mode["success"]["mode"]
        image_type= required_mode["success"]["image_type"]
    data=[str("/media/apps/%s/%s/login_images/%s.jpg") %(mode,image_type,each)  
                for each in LOGIN_IMAGES ]
    if request.method=="POST":
        return gs("POST",req_dict(request.POST),{"data":data})
         
             
             
             
def req_dict(request_method):
    return dict([(e,request_method.get(e)) for e in request_method])

def get_error(request_type,
              request_data,
              message,error_fields=None):
    return {"result":"error",
            "message":message,
            "request_type":request_type,
            "request_data":request_data,
            "error_fields":error_fields
            }
    
def get_success(request_type,request_data,json_data):
    return {
            "request_type":request_type,
            "request_data":request_data,
            "result":"success",
            "json":json_data,
            }

gs,ge=get_success, get_error

def mode_require(request,):
    """Will make mode require from android and ios,
    Also if request says image_type is mandatory , checks that as well
    """
    #Another common operation , mode is required.
    mode=request.POST.get("mode")
    if mode not in ["android","ios"]:
        return {"error":ge("POST",dict(request.POST),"mode can be android or ios only",
                  error_fields=["mode"])
                } 
    #Another common operation where mode is required ++ 
    
    image_type=request.POST.get("image_type","None")
    if image_type:
        if mode == "android" and image_type not in ALLOWED_ANDRIOD_IMAGE_TYPE:
            ## TODO Severe error 
            return  {"error":ge("POST",dict(request.POST),",".join(ALLOWED_ANDRIOD_IMAGE_TYPE) +"allowed",
                      error_fields=["mode"])
                     }
        if mode == "ios" and image_type not in ALLOWED_IOS_IMAGE_TYPE:
            ## TODO Severe error 
            return  {"error":ge("POST",dict(request.POST),",".join(ALLOWED_IOS_IMAGE_TYPE) +"allowed",
                      error_fields=["mode"])
                     }
    
    return {"success":{"mode":mode,"image_type":image_type}}    