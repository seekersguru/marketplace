def get_error(request_type,
              request_data,
              message,json_data=None):
    return {"result":"error",
            "message":message,
            "request_type":request_type,
            "request_data":request_data,
            "json":json_data
            }
    
def get_success(request_type,request_data,json_data):
    return {
            "request_type":request_type,
            "request_data":request_data,
            "result":"success",
            "json":json_data,
            }
    