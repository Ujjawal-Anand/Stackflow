import requests
import json

from django.shortcuts import render
from django.views.generic import FormView
from django.contrib import messages

from .models import ApiData
from .forms import ApiDataForm

# Create your views here.

class Question(object):
    def __init__(self, data):
	    self.__dict__ = data
class ApiDataFormView(FormView):
    form_class = ApiDataForm
    template_name = 'api_data_form.html'
    success_url = '/'
    questions = []
    endpoint = 'https://api.stackexchange.com/2.2/search/advanced'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["questions"] = self.questions 
        return context
    

    def form_valid(self, form):
        result = {}
        post_data = self.request.POST.dict()
        post_data.pop('csrfmiddlewaretoken', None)
        post_data['site'] = 'stackoverflow'
        response = requests.get(url=self.endpoint, params=post_data)
        
        if response.status_code == 200:
            try:
                result = response.json()['items']
                messages.success(self.request, 'Successfully fetched data')
            except json.decoder.JSONDecodeError as e:
                print(e)
                messages.error(self.request, 'Error in decoding json data')
        else:
            
            if response.status_code == 404:
                result['message'] = 'No entry found'
                messages.info(self.request, '404 error')
            else:
                message = 'The Stack API is not available at the moment. Please try again later.'
                messages.info(self.request, message)
        print(result)
        
        for data in result:
            question = Question(data)
            self.questions.append(question)
        print(self.questions[0].tags)
    
        return super().form_valid(form)
