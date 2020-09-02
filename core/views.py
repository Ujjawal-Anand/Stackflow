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
    '''
      Question class will be used to deswrialize json data 
    '''
    def __init__(self, data):
	    self.__dict__ = data

# cache requests, expires after 180 seconds
requests_cache.install_cache('stackflow_cache', backend='sqlite', expire_after=180)

class ApiDataFormView(FormView):
    '''
    Api Data form view, renders form and fetched data as well
    '''
    form_class = ApiDataForm
    template_name = 'api_data_form.html'
    success_url = '/'
    endpoint = 'https://api.stackexchange.com/2.2/search/advanced'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get results data (fetched from api) from session
        results = self.request.session.get('results', [])
        # get page number from get queryset
        page = self.request.GET.get('page_num', None)
        # this is used to show next page of data
        if len(results) > 0 and page is not None:
            # deserialize results data to questions and add to context
            context['questions'] = self.get_paginated_data(data_list=self.deserialize_data(results=results))
        
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        get_data = self.request.GET.dict()

        page = self.request.GET.get('page_num', None)
   
        if len(get_data) > 0 and not page:
            # add site value
            get_data['site'] = 'stackoverflow'
            # fetch data from api using data from get requests as params
            results = self.fetch_data(params=get_data)
            # deserialize data
            question_list = self.deserialize_data(results)
            # paginate data
            context['questions'] = self.get_paginated_data(data_list=question_list)
            # save data to session, this data will be used to show paginated data
            self.request.session['results'] = results
            context['form'] = self.form_class(self.request.GET)
    
            return render(self.request, self.template_name, context=context)

        return render(self.request, self.template_name, context)

    def deserialize_data(self, results):
        '''
         this will deserialize fetched json data to question object
        '''
        return [Question(data=result) for result in results]

    @method_decorator(ratelimit(key='ip', rate='5/m', method=ratelimit.ALL))
    @method_decorator(ratelimit(key='ip', rate='100/d', method=ratelimit.ALL))
    def ratelimit_counter(self, request):
        '''
        an empty function for ratelimit counter, a call to this function will incresase the ratelimit counter
        '''
        pass


    def fetch_data(self, params):
        '''
        a function to fetch data from stackoverflow api using python requests
        '''
        # var provided by ratelimit decorator to limit api call
        was_limited = getattr(self.request, 'limited', False)
        results = []
        # check user has exauseted the rate limit
        if was_limited:
            messages.error(self.request, 'You have exaused your rate limit, please try after some time')
            return results
        # fetch data using python requests
        response = requests.get(url=self.endpoint, params=params)
        # check whether response is cached data and increase ratelimit accordingly
        # if not response from cache - do not increase rate counter
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
        page = self.request.GET.get('page_num', 1)
        paginator = Paginator(data_list, settings.QUESTIONS_PER_PAGE)
        try:
            paginated_data = paginator.page(page)
        except PageNotAnInteger:
            paginated_data = paginator.page(1)
        except EmptyPage:
            paginated_data = paginator.page(paginator.num_pages)
        return paginated_data
