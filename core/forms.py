from django import forms

from crispy_forms.helper import FormHelper

from .models import ApiData

class DateInput(forms.DateInput):
    input_type = 'date'

class ApiDataForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
    
    class Meta:
        model = ApiData
        exclude = ()
        widgets = {
            'fromdate': DateInput(),
            'todate': DateInput(),
            'min_date': DateInput(),
            'max_date': DateInput()
        }
