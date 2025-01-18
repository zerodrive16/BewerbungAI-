import json
import asyncio
import subprocess

from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token
from .models import Data
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DataSerializer
#from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

from .Text_Preprocessing.spacy_summarizer import textSummarizationJobDescription, textSummarizationPersonalInformation
from .Text_Preprocessing.openai_request import openAIRequest
from .Text_Preprocessing.regex_processing import performRegex
from .Text_Preprocessing.storeDatabase import databaseStorage


# Create your views here.

resume_data = {}
application_data = {}
file_data ={}


def home(request):
    return render(request, 'index.html')


@api_view(['GET'])
def dataset_api(request):
    data = Data.objects.all()
    if not data.exists():
        return Response({"message": "No data found in the database"}, status=404)

    # Use the serializer to convert data into JSON
    data_serialized = DataSerializer(data, many=True)

    # Return the serialized data as JSON in the response
    return Response(data_serialized.data)


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

            AIOutput, app_final, personal_final = generatedJobApplicationLetter(resume_data, application_data)
            print(AIOutput)

            databaseStorage(resume_data, application_data, app_final, personal_final, AIOutput)

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


def generatedJobApplicationLetter(resume_data, application_data):
    # Consideration of both finished API's (with data)

    # Text Preprocessing Job Description
    # Summarize specific fields
    jDFieldsSummarize = ["job"]

    jDResults = {}

    for key, value in application_data.items():
        if isinstance(value, str):
            jDProcessedValue = performRegex(value)

            if key in jDFieldsSummarize:
                jDResults[key] = {
                    "processed": jDProcessedValue,
                    "summary": textSummarizationJobDescription(jDProcessedValue)
                }
            else:
                jDResults[key] = jDProcessedValue
        else:
            jDResults[key] = value


    finalJobDescription = jDResults

    # Text Preprocessing Personal Information
    # Summarize specific fields
    pIFieldsSummarize = ["experience", "education", "skills", "interests"]

    pIResults = {}

    for key, value in resume_data.items():
        if isinstance(value, str):
            pIProcessedValue = performRegex(value)

            if key in pIFieldsSummarize:
                pIResults[key] = {
                    "processed": pIProcessedValue,
                    "summary": textSummarizationPersonalInformation(pIProcessedValue)
                }
            else:
                pIResults[key] = pIProcessedValue
        else:
            pIResults[key] = value

    finalPersonalDescription = pIResults

    # OpenAI request
    openAIOutput = openAIRequest(resume_data, application_data, finalJobDescription, finalPersonalDescription)
    return(openAIOutput, finalJobDescription, finalPersonalDescription)


file_data = None  # Initialize file_data globally

@api_view(["POST", "GET"])
def download(request):
    global file_data

    if request.method == "POST":
        try:
            process = subprocess.run(
                ["python", "WebApplication/Text_Preprocessing/Pretrain Dataset/helloWorld.py"],
                check=True,
                capture_output=True,
                text=True,
            )
            file_data = {"output": process.stdout}

            # Skip serialization, directly return the processed data as JSON
            return Response({"message": "Data processed successfully", "data": file_data}, status=200)

        except subprocess.CalledProcessError as e:
            return Response({"error": str(e)}, status=500)

    elif request.method == "GET":
        # Return the raw data directly in the JSON response
        if file_data:
            return Response({"message": "GET request received", "data": file_data}, status=200)
        else:
            return Response({"message": "No data available"}, status=200)

    # Fallback for unsupported methods
    return Response({"error": "Method not allowed"}, status=405)

