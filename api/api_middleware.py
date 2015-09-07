import urllib
from market_place.settings import MEDIA_PATH
import datetime
class ApiMiddleware:
    def process_request(self,request):
        if request.path.startswith("/api/"):
            request.is_api=True
            request_post=request.POST
            req_post_copy=request_post.copy()
            for each in request_post:
                req_post_copy[each]=urllib.unquote(request_post[each])
            request.POST=req_post_copy
            
            f=open(MEDIA_PATH.replace("media","templates/console.html"),"a")
            data=str(datetime.datetime.now())[:-7] + " : "+ str(request.path)+"<br>"+"<br/>".join(["%s => %s "%(e,request.POST[e]) for e in request.POST]) + "<hr/>" +"\n"
            f.write(data)
            f.close
            f=open(MEDIA_PATH.replace("media","templates/console.html"),"r")
            len_files= len(f.readlines())
            f.close()
            if len_files>1000:
                f=open(MEDIA_PATH.replace("media","templates/console.html"),"w")
                f.write("""<a href ="/clear_console/"> Clear Console </a> <br/><br/><br/>""" + data)
                f.close()
        print "POST Modified",request.path
        for k,v in  dict(request.POST).iteritems():
            print k , v 
        else:
            request.is_api=False
            
 
    def process_template_response(self,request , response):
        if request.is_api:
            print "do common stuff in template response"
        return response
#     def process_response(self,request,response):
#         if request.is_api:
#             print "do common stuff in  response"

