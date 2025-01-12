from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView

"""
Functions home and runMLScript(staying after the view.)
manage the output and if needed(function runMLScript) add it in the html.

"""
urlpatterns = [
    path('', views.home, name='home'),
    path('get-csrf-token', views.get_csrf_token, name='get_csrf_token'),
    path('resume/api', views.resume_api, name='resume_api'),
    path('application/api', views.application_api, name='application_api'),
    path('dataset/api', views.dataset_api, name='dataset_api'),
    path('download/api', views.download, name='download'),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]
