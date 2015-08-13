from django.db import models

class VendorManager(models.Manager):
    def get_queryset(self):
        return super(VendorManager, self).get_queryset().filter(active=1)