def get_error(request_type,
              request_data,
              message):
    return {"result":"error",
            "message":message,
            "request_type":request_type,
            "request_data":request_data
            }
    
def get_success(request_type,request_data,json):
    return {
            "request_type":request_type,
            "request_data":request_data,
            "result":"success",
            "json":json,
            }
    