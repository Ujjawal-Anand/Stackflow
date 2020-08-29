import requests
import json

from django.conf import settings
from django.shortcuts import render
from django.views.generic import FormView, View
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.decorators import method_decorator

import requests_cache
from ratelimit.decorators import ratelimit

from .models import ApiData
from .forms import ApiDataForm

# Create your views here.

class Question(object):
    def __init__(self, data):
	    self.__dict__ = data

requests_cache.install_cache('stackflow_cache', backend='sqlite', expire_after=180)

class ApiDataFormView(FormView):
    form_class = ApiDataForm
    template_name = 'api_data_form.html'
    ratelimit_increment = True
    success_url = '/'
    endpoint = 'https://api.stackexchange.com/2.2/search/advanced'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = self.request.session.get('results', [])
        page = self.request.GET.get('page', None)

        if len(results) > 0 and page is not None:
            context['questions'] = self.get_paginated_data(data_list=self.deserialize_data(results=results))
        
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        get_data = self.request.GET.dict()
        get_data.pop('csrfmiddlewaretoken', None)
        print(get_data)
        
        if len(get_data) > 0:
            get_data['site'] = 'stackoverflow'
            results = self.fetch_data(params=get_data)
            question_list = self.deserialize_data(results)
        
            context['questions'] = self.get_paginated_data(data_list=question_list)
            self.request.session['results'] = results
    
            return render(self.request, self.template_name, context=context)

        return render(self.request, self.template_name, context)

    def deserialize_data(self, results):
        return [Question(data=result) for result in results]

    @method_decorator(ratelimit(key='ip', rate='5/m', method=ratelimit.ALL))
    @method_decorator(ratelimit(key='ip', rate='100/d', method=ratelimit.ALL))
    def ratelimit_counter(self, request):
        pass


    def fetch_data(self, params):
        was_limited = getattr(self.request, 'limited', False)
        results = []
        if was_limited:
            messages.error(self.request, 'You have exaused your rate limit, please try after some time')
            return results
        
        response = requests.get(url=self.endpoint, params=params)
        if not response.from_cache:
            self.ratelimit_counter(request=self.request)

        if response.status_code == 200:
            try:
                results = response.json()['items']
                messages.success(self.request, 'Successfully fetched data')
            except json.decoder.JSONDecodeError as e:
                print(e)
                messages.error(self.request, 'Error in decoding json data')
        else:
            
            if response.status_code == 404:
                messages.info(self.request, '404 error')
            else:
                message = 'The Stack API is not available at the moment. Please try again later.'
                messages.info(self.request, message)
        return results
    
    def get_paginated_data(self, data_list=[]):
        paginated_data = []
        page = self.request.GET.get('page', 1)
        paginator = Paginator(data_list, settings.QUESTIONS_PER_PAGE)
        try:
            paginated_data = paginator.page(page)
        except PageNotAnInteger:
            paginated_data = paginator.page(1)
        except EmptyPage:
            paginated_data = paginator.page(paginator.num_pages)
        return paginated_data
