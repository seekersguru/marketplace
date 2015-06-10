from django.forms import ModelForm
from models import Banquet
class BanquetForm(ModelForm):
    class Meta:
        model = Banquet