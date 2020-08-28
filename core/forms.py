from django import forms

from .models import ApiData
from .widgets import DatePickerInput

class ApiDataForm(forms.ModelForm):
    min_date = forms.DateTimeField(
        input_formats=['%d/%m/%Y'], 
        widget=DatePickerInput()
    )
    
    class Meta:
        model = ApiData
        exclude = ()
