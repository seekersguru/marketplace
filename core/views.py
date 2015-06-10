

# Create your views here.
##Create Banquet method here.
from core.forms import BanquetForm
from django.template.response import TemplateResponse
from core.models import Banquet


from vendor.vendor_rules import banquet_rule
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def banquets(request):
    
    return TemplateResponse (request,'banquets.html',
                             {"rules":banquet_rule ,
                             "message":"Some Message on the top ",
                             "message_class":""
                            }
                             )



def add_banquet(request):
    if request.method == 'GET':
        form = BanquetForm()
    else:
        # A POST request: Handle Form Upload
        # Bind data from request.POST into a PostForm
        form = BanquetForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
                  
            name = form.cleaned_data['name']
            plotno = form.cleaned_data['plotno']
            city = form.cleaned_data['city']
            pincode = form.cleaned_data['pincode']
            area = form.cleaned_data['area']
            post = Banquet.objects.create(name=name, 
                                          plotno=plotno,
                                          city=city,
                                          pincode=pincode,
                                          area=area,
                                          )
            

    banquets = Banquet.objects.all()
    return TemplateResponse (request,'banquet_add.html',{"form":form,"banquets":banquets})