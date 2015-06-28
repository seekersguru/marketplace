from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Here create Banquet Model
class Customer(models.Model):
    #email password
    user = models.OneToOneField(User, primary_key=True)
    groom_name = models.CharField(max_length=100)
    bride_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)

    @classmethod
    def create(cls, 
               email, 
               password, 
               groom_name,
               bride_name,):
        User.objects.get("username")
        # do something with the book
        return customer
    
         
    def __unicode__(self):
        return self.name
