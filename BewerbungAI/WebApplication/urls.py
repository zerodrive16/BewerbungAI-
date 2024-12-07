from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView

"""
Functions home and runMLScript(staying after the view.)
manage the output and if needed(function runMLScript) add it in the html.

"""
urlpatterns = [
    path('', views.home, name='home'),
    path('backend', views.helloWorldScript, name='helloWorldScript'),
    #path('backend', views.runMLScript, name='runMLScript'),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html'))
]
