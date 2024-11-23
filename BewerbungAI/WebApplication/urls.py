from django.urls import path
from . import views

"""
Functions home and runMLScript(staying after the view.)
manage the output and if needed(function runMLScript) add it in the html.

"""
urlpatterns = [
    path('', views.home, name='home'),
    path('backend', views.runMLScript, name='runMLScript')
]
