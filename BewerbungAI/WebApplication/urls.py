from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView
from .views import export_users_from_keycloak

"""
Functions home and runMLScript(staying after the view.)
manage the output and if needed(function runMLScript) add it in the html.

"""
urlpatterns = [
    # Login Page
    path('', views.home, name='home'),
    # CSRF Token parse for API calls
    path('get-csrf-token', views.get_csrf_token, name='get_csrf_token'),
    # Personal Information endpoint for retrieving data
    path('resume/api', views.resume_api, name='resume_api'),
    # Job Description endpoint for retrieving data
    path('application/api', views.application_api, name='application_api'),
    # Dataset endpoint containing Personal Information, Job Description and AI-generated Job Application Letter
    path('dataset/api', views.dataset_api, name='dataset_api'),
    # User Profile dataset containing the login credentials
    path('userProfile/api', views.user_profile_api, name='user_profile_api'),
    # Download endpoint to retrieve the output as a file
    path('download/api', views.download, name='download'),
    path('export-users/', views.export_users_from_keycloak, name='export_users_from_keycloak'),
    path('email', views.get_current_email, name='get_current_email'),
    # Open up React Template Localhost
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]
