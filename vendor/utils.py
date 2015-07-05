# TODO , DB Dynamic , processs from backend.

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
    return [
    ## Do not change banquet and caterer at 1 and 2 cindition to show packages
        create_vendor_meta(1,"Banquets","banquets","Banquet contents"),
        create_vendor_meta(2,"Caterers","caterers","Caterer contents"),
        create_vendor_meta(3,"Decorators","decorators","Decorator contents"),
        create_vendor_meta(4,"Photographers","photographers","Photographer contents"),
        create_vendor_meta(5,"Hotels","hotels","Hotels contents"),
        create_vendor_meta(6,"Others","others","Others contents"),
    ]
VENDOR_CATEGORIES=[(each.get("key"),each.get("name")) for each in get_vendor_meta()]