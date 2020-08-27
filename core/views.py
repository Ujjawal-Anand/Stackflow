from django.shortcuts import render
from django.views.generic import FormView

from .models import ApiData
from .forms import ApiDataForm

# Create your views here.

class ApiSearchListView(FormView):
    
