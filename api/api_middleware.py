class ApiMiddleware:
    def process_request(self,request):
        if request.path.startswith("/api/"):
            request.is_api=True
            print "do common stuff in request "
        else:
            request.is_api=False
            
 
    def process_template_response(self,request , response):
        if request.is_api:
            print "do common stuff in template response"
        return response
#     def process_response(self,request,response):
#         if request.is_api:
#             print "do common stuff in  response"

