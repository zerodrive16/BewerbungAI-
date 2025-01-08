import json
import os
import subprocess

from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt


# Create your views here.

resume_data = {}
application_data = {}


def home(request):
    return render(request, 'index.html')


def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})


def resume_api(request):
    global resume_data

    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            print(data)
            value = data.get('value', 'N/A')
            name = value.get('name', 'N/A')
            surname = value.get('surname', 'N/A')
            birthday = value.get('birthday', 'N/A')
            birthplace = value.get('birthplace', 'N/A')
            nationality = value.get('nationality', 'N/A')
            address = value.get('address', 'N/A')
            phone = value.get('phone', 'N/A')
            email = value.get('email', 'N/A')
            experience = value.get('experience', 'N/A')
            education = value.get('education', 'N/A')
            skills = value.get('skills', 'N/A')
            languages = value.get('languages', 'N/A')
            interests = value.get('interests', 'N/A')

            resume_data = {
                'name': name,
                'surname': surname,
                'birthday': birthday,
                'birthplace': birthplace,
                'nationality': nationality,
                'address': address,
                'phone': phone,
                'email': email,
                'experience': experience,
                'education': education,
                'skills': skills,
                'languages': languages,
                'interests': interests,
            }
            print(resume_data)
            return JsonResponse({'message': 'POST request received', 'data': resume_data}, status=200)
        except Exception as e:
            return JsonResponse({'error': 'Invalid data', 'details': str(e)}, status=400)

    elif request.method == 'GET':
        if resume_data:
            return JsonResponse({'message': 'GET request received', 'data': resume_data}, status=200)
        else:
            return JsonResponse({'message': 'No data available'}, status=200)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def application_api(request):
    global application_data

    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            print(data)
            value = data.get('value', 'N/A')
            job = value.get('job', 'N/A')

            application_data = {
                'job': job
            }
            print(application_data)
            return JsonResponse({'message': 'POST request received', 'data': application_data}, status=200)
        except Exception as e:
            return JsonResponse({'error': 'Invalid data', 'details': str(e)}, status=400)

    elif request.method == 'GET':
        if application_data:
            return JsonResponse({'message': 'GET request received', 'data': application_data}, status=200)
        else:
            return JsonResponse({'message': 'No data available'}, status=200)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

