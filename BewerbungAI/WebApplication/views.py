import json
import subprocess

from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token
from .models import Data
from .serializers import DataSerializer
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt


# Create your views here.

resume_data = {}
application_data = {}
file_data ={}

def home(request):
    return render(request, 'index.html')


def dataset_api(request):
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
            print("Hello World 1")
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
            manager_name = value.get('manager_name', 'N/A')
            company_name = value.get('company_name', 'N/A')
            company_address = value.get('company_address', 'N/A')
            company_city = value.get('company_city', 'N/A')
            company_zip_code = value.get('company_zip_code', 'N/A')
            job_field_name = value.get('job_field_name', 'N/A')
            job = value.get('job', 'N/A')

            application_data = {
                'manager_name': manager_name,
                'company_name': company_name,
                'company_address': company_address,
                'company_city': company_city,
                'company_zip_code': company_zip_code,
                'job_field_name': job_field_name,
                'job': job
            }
            print("Hello World 2")
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


data_store = {
    'resume': None,
    'job_description': None,
}


def combined_api(request):
    if request.method == 'POST':
        try:
            # Parse incoming data
            data = json.loads(request.body.decode('utf-8'))
            data_type = data.get('type', None)  # 'resume' or 'job_description'
            value = data.get('value', 'N/A')

            # Fetch or create the database record
            data_entry, created = Data.objects.get_or_create(id=1)  # Using a single entry for simplicity

            # Update the respective field
            if data_type == 'resume':
                data_entry.resume = value
            elif data_type == 'job_description':
                data_entry.job_description = value
            else:
                return JsonResponse({'error': 'Invalid data type'}, status=400)

            # Save the updated entry
            data_entry.save()

            # Check if both fields are filled
            if data_entry.resume and data_entry.job_description:
                combined_data = {
                    'resume': data_entry.resume,
                    'job_description': data_entry.job_description,
                }

                # Optional: Process the combined data (e.g., send to OpenAI)

                return JsonResponse({
                    'message': 'Both data received and processed',
                    'combined_data': combined_data
                }, status=200)

            return JsonResponse({'message': f'{data_type} data received. Waiting for the other data.'}, status=200)
        except Exception as e:
            return JsonResponse({'error': 'Invalid data', 'details': str(e)}, status=400)

    elif request.method == 'GET':
        try:
            data_entry = Data.objects.get(id=1)  # Fetch the existing entry
            response_data = {
                'resume': data_entry.resume,
                'job_description': data_entry.job_description,
            }
            return JsonResponse({'current_data': response_data}, status=200)
        except Data.DoesNotExist:
            return JsonResponse({'current_data': 'No data available'}, status=200)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def generatedJobApplicationLetter():
    # Consideration of both finished API's (with data)
    pass


file_data = None


@api_view(["POST", "GET"])
def download(request):
    global file_data
    print("start")
    if request.method == "POST":
        try:
            process = subprocess.run(
                ["python", "WebApplication/Text_Preprocessing/Pretrain Dataset/helloWorld.py"],
                check=True,
                capture_output=True,
                text=True
            )
            file_data = {"output": process.stdout}

            # Serialize the data
            serializer = DataSerializer(data=file_data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Data processed and saved", "data": serializer.data}, status=200)
            else:
                return Response({"error": serializer.errors}, status=400)
        except subprocess.CalledProcessError as e:
            return Response({"error": str(e)}, status=500)

    elif request.method == "GET":
        if file_data:
            serializer = DataSerializer(file_data)
            return Response({'message': 'GET request received', 'data': serializer.data}, status=200)
        else:
            return Response({'message': 'No data available'}, status=200)

    else:
        return Response({'error': 'Method not allowed'}, status=405)

