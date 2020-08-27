from django.shortcuts import render
from django.views.generic import FormView

from .models import ApiData
from .forms import ApiDataForm

# Create your views here.

class ApiDataFormView(FormView):
    form_class = ApiDataForm
    template_name = 'api_data_form.html'
