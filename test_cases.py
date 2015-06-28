import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "market_place.settings")

django.setup()

from django.test.client import Client
c = Client()

tes_api="customer_registration"

if tes_api=="customer_registration":
    response = c.post('/api/customer_registration/', {'username': 'john', 'password': 'smith'})

