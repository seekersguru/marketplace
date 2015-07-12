# TODO , DB Dynamic , processs from backend.
from vendor.models import Category

def create_vendor_meta(cat_id,name,key,div_label,fields=None):
    return {
            "cat_id":cat_id,
            "name":name,
            "key":key,
            "div_label":div_label,
            "fields":fields
            }
        
#TODO arrange and make dynamic
def get_vendor_meta():
    cats=Category.objects.all()
    return [
    ## Do not change banquet and caterer at 1 and 2 cindition to show packages
        create_vendor_meta(str(e.id),str(e.name),str(e.key),str(e.name)+" contents") for e in cats
    ] 
VENDOR_CATEGORIES=[(each.get("key"),each.get("name")) for each in get_vendor_meta()]