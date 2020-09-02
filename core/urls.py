from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.ApiDataFormView.as_view(), name='apt-data-form'),
    path('details/', TemplateView.as_view(template_name="details.html"), name="details"),
    path('about/', TemplateView.as_view(template_name="about.html"), name="about")
]
