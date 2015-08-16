import urllib
class ApiMiddleware:
    def process_request(self,request):
        if request.path.startswith("/api/"):
            request.is_api=True
            request_post=request.POST
            req_post_copy=request_post.copy()
            for each in request_post:
                req_post_copy[each]=urllib.unquote(request_post[each])
            request.POST=req_post_copy
	    print "POST Modified", dict(request.POST)
        else:
            request.is_api=False
            
 
    def process_template_response(self,request , response):
        if request.is_api:
            print "do common stuff in template response"
        return response
#     def process_response(self,request,response):
#         if request.is_api:
#             print "do common stuff in  response"

