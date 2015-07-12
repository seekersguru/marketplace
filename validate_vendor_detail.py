import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "market_place.settings")
django.setup()

import json 
from vendor.models import Vendor 
vendors = Vendor.objects.all()

for vendor in vendors:
    try:
        vendor_parsed=json.loads(vendor.dynamic_info)
    except:
        #print vendor.user.username
        print 111111111111
        import pdb;pdb.set_trace()
    
    ## TOTDO Handle types for above and rest (Mature it more)
    try:
        ## Handle null value exceptions
        vendor_parsed['info']['starting_price']
        vendor_parsed['info']['top_name']
        vendor_parsed['info']['hero_imgs']
        vendor_parsed['info']['video_links']
        vendor_parsed['info']['top_address']
        vendor_parsed['info']['contact']
        try:
            if vendor.user.username != vendor_parsed['info']['email']:
                raise Exception("Vendor User Email is not same ")
        except:
            print "Set the value soem how !!"
            vendor_parsed["info"]["email"]=vendor.user.username
            print 22222222222
            import pdb;pdb.set_trace()
            ##TODO 
            ###vendor.dynamic_info=str(vendor_parsed)
            ###vendor.save()
            
    except Exception as e:
        print  333333333,e
        import pdb;pdb.set_trace()
        
