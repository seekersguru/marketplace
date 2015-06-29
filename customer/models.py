from django.db import models
from django.contrib.auth.models import User
from api.utils import get_error as ge , get_success as gs ,req_dict
# Create your models here.
from django.db import transaction
"""
https://docs.djangoproject.com/en/1.8/topics/db/transactions/
Atomicity is the defining property of database transactions. atomic allows us to create a block of code within 
which the atomicity on the database is guaranteed. If the block of code is successfully completed, the changes are 
committed to the database. If there is an exception, the changes are rolled back.
"""
from django.core.signing import Signer
signer = Signer()
#value = signer.sign('My string')
#original = signer.unsign(value)
#Here create Banquet Model
class Customer(models.Model):
    #email password
    user = models.OneToOneField(User, primary_key=True)
    groom_name = models.CharField(max_length=100)
    bride_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    identifier = models.CharField(max_length=512)
    fbid = models.CharField(max_length=1024,default="")
    gid =models.CharField(max_length=1024,default="")
    
 
    @classmethod
    @transaction.atomic # @Nishant see if its effect speed @Amit dash 
    def create(cls,
               request, 
               ):
        email = request.POST.get('email').strip().lower()
        password = request.POST.get('password')
        groom_name = request.POST.get('groom_name')
        bride_name = request.POST.get('bride_name')
        contact_number = request.POST.get('contact_number')
        
        user = User.objects.filter(username=email)
        if user:
            return ge("POST",req_dict(request.POST),"email already exists", error_fields=['email'])


        if len(password)<3:
            return ge("POST",req_dict(request.POST),"password too short", error_fields=['password']) 
 
        # As we using transactions, no need to error handle. 
        # In case of error all will revert
        user = User.objects.create_user(email, email, password)
        customer=Customer(user=user,groom_name=groom_name,
                 bride_name=bride_name,
                 contact_number=contact_number,
                 identifier=signer.sign(email))
        # do something with the book
        customer.save()
        
        return gs("POST",req_dict(request.POST),{"identifier":customer.identifier})
    
         

