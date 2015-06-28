from django.db import models
from django.contrib.auth.models import User
from api.utils import get_error as ge , get_success as gs
# Create your models here.
from django.db import transaction
"""
https://docs.djangoproject.com/en/1.8/topics/db/transactions/
Atomicity is the defining property of database transactions. atomic allows us to create a block of code within 
which the atomicity on the database is guaranteed. If the block of code is successfully completed, the changes are 
committed to the database. If there is an exception, the changes are rolled back.
"""

#Here create Banquet Model
class Customer(models.Model):
    #email password
    user = models.OneToOneField(User, primary_key=True)
    groom_name = models.CharField(max_length=100)
    bride_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)

    @classmethod
    @transaction.atomic # @Nishant see if its effect speed @Amit dash 
    def create(cls,
               request, 
               email, 
               password, 
               groom_name,
               bride_name,):
        user = User.objects.filter(username=email)
        if user:
            return ge("POST",
                      dict(request.POST),
                      "email already exists"
                      )
        
        # do something with the book
        return customer
    
         
    def __unicode__(self):
        return self.name
