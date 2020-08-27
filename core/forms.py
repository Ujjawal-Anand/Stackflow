from django.forms import ModelForm

from .models import ApiData

class ApiDataForm(ModelForm):
    
    class Meta:
        model = ApiData
        exclude = ()
