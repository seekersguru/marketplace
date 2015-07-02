ALLOWED_ANDRIOD_IMAGE_TYPE=["drawable-hdpi", "drawable-xhdpi", "drawable-xxhdpi","drawable-xxxhdpi",]
ALLOWED_IOS_IMAGE_TYPE=["2x", "3x",]
from utils import ALLOWED_ANDRIOD_IMAGE_TYPE,ALLOWED_IOS_IMAGE_TYPE


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
    