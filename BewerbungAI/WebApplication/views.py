import json
import os
import subprocess

from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token
from .models import Data
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt


# Create your views here.

resume_data = {}
application_data = {}


def home(request):
    return render(request, 'index.html')


def dataset():
    data = list(Data.objects.all())
    return JsonResponse(data, safe=False)


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
            first_name = value.get('first_name', 'N/A')
            last_name = value.get('last_name', 'N/A')
            birthday = value.get('birthday', 'N/A')
            address = value.get('address', 'N/A')
            city = value.get('city', 'N/A')
            zipcode = value.get('zipcode', 'N/A')
            phone = value.get('phone', 'N/A')
            email = value.get('email', 'N/A')
            date = value.get('date', 'N/A')
            experience = value.get('experience', 'N/A')
            education = value.get('education', 'N/A')
            skills = value.get('skills', 'N/A')
            interests = value.get('interests', 'N/A')

            resume_data = {
                'first_name': first_name,
                'last_name': last_name,
                'birthday': birthday,
                'address': address,
                'city': city,
                'zipcode': zipcode,
                'phone': phone,
                'email': email,
                'date': date,
                'experience': experience,
                'education': education,
                'skills': skills,
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


def download(request):
    if request.method == "POST":
        try:
            subprocess.run(["python", "WebApplication/Text_Preprocessing/Pretrain Dataset/helloWorld.py"], check=True)
            return JsonResponse({"message": "Script executed successfully!"}, status=200)
        except subprocess.CalledProcessError as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request method."}, status=400)

