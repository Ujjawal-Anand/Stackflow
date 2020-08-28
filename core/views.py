import requests
import json

from django.shortcuts import render
from django.views.generic import FormView
from django.contrib import messages

from .models import ApiData
from .forms import ApiDataForm

# Create your views here.

class ApiDataFormView(FormView):
    form_class = ApiDataForm
    template_name = 'api_data_form.html'
    success_url = '/'
    endpoint = 'https://api.stackexchange.com/2.2/search/advanced'


    def form_valid(self, form):
        result = {}
        post_data = self.request.POST.dict()
        post_data.pop('csrfmiddlewaretoken', None)
        post_data['site'] = 'stackoverflow'
        response = requests.get(url=self.endpoint, params=post_data)
        
        if response.status_code == 200:
            try:
                result = response.json()
                result['success'] = True
                messages.success(self.request, 'Successfully fetched data')
            except json.decoder.JSONDecodeError as e:
                print(e)
                messages.error(self.request, 'Error in decoding json data')
        else:
            result['success'] = False
            
            if response.status_code == 404:
                result['message'] = 'No entry found'
                messages.info(self.request, '404 error')
            else:
                message = 'The Stack API is not available at the moment. Please try again later.'
                messages.info(self.request, message)
                result['message'] = message
        print(result)
        return super().form_valid(form)
