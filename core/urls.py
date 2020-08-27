from django.urls import path

from . import views

urlpatterns = [
    path('', views.ApiDataFormView.as_view(), name='apt-data-form')
]
