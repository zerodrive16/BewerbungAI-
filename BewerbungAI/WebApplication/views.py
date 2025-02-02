import json
import asyncio
import subprocess
import requests

from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token
from .models import Data
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DataSerializer, UserProfileSerializer

# Imports needed to format the job description and personal information to a Job Application Letter
from .Text_Preprocessing.spacy_summarizer import textSummarizationJobDescription, textSummarizationPersonalInformation
from .Text_Preprocessing.openai_request import openAIRequest
from .Text_Preprocessing.regex_processing import performRegex
from .Text_Preprocessing.storeDatabase import databaseStorage

from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile


# Store the results here
resume_data = {}
application_data = {}
file_data = {}

# Redirect to the index.html to open up the Web Application
def home(request):
    return render(request, 'index.html')


# Serializing the Instances in the Database to JSON
@api_view(['GET'])
def dataset_api(request):
    data = Data.objects.all()
    if not data.exists():
        return Response({"message": "No data found in the database"}, status=200)

    # Use the serializer to convert data into JSON
    data_serialized = DataSerializer(data, many=True)

    # Return the serialized data as JSON in the response
    return Response(data_serialized.data)


@api_view(['GET'])
def user_profile_api(request):
    user_data = UserProfile.objects.all()
    serialized_data = UserProfileSerializer(user_data, many=True)
    return Response(serialized_data.data)


# CSRF Token request
def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})


# Retrieval of personal information in endpoint /resume/api
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


# Retrieval of job description in endpoint /application/api
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

            AIOutput, app_final, personal_final = asyncio.run(
                generatedJobApplicationLetter(resume_data, application_data)
            )
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


# Generates the job application letter
async def generatedJobApplicationLetter(resume_data, application_data):
    # Consideration of both finished APIs (with data)

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
                    "summary": await textSummarizationJobDescription(jDProcessedValue)
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
                    "summary": await textSummarizationPersonalInformation(pIProcessedValue)
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

@csrf_exempt  # Use with caution; it's better to handle CSRF tokens properly
def export_users_from_keycloak(request):
    if request.method == 'POST':  # Only allow POST requests
        try:
            # Step 1: Fetch Access Token from Keycloak
            token_url = "http://localhost:8080/realms/master/protocol/openid-connect/token"
            client_id = "admin-cli"
            client_secret = "tMM0oz1KOxuNkVkyGcZkRWW70RGNnITF"
            payload = {
                "username": "admin",  # Replace with your Keycloak admin username
                "password": "admin",  # Replace with your Keycloak admin password
                "grant_type": "password",
                "client_id": client_id,
                "client_secret": client_secret,
            }

            token_response = requests.post(token_url, data=payload)
            if token_response.status_code != 200:
                return JsonResponse(
                    {"status": "error", "message": "Failed to fetch access token from Keycloak."},
                    status=token_response.status_code
                )

            access_token = token_response.json().get('access_token')
            if not access_token:
                return JsonResponse(
                    {"status": "error", "message": "Access token is missing from the response."},
                    status=500
                )

            # Step 2: Fetch Users from Keycloak
            users_url = "http://localhost:8080/admin/realms/myrealm/users"
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json",
            }

            users_response = requests.get(users_url, headers=headers)
            if users_response.status_code != 200:
                return JsonResponse(
                    {"status": "error", "message": "Failed to fetch users from Keycloak."},
                    status=users_response.status_code
                )

            users = users_response.json()
            for user in users:
                # Step 3: Extract the necessary fields for your UserProfile model
                keycloak_id = user['id']
                username = user.get('username')
                email = user.get('email', '')
                first_name = user.get('firstName', '')
                last_name = user.get('lastName', '')
                print(f"email:{email}")
                # Save or update the user profile in the database
                UserProfile.objects.update_or_create(
                    keycloak_id=keycloak_id,
                    defaults={
                        'username': username,
                        'email': email,
                        'first_name': first_name,
                        'last_name': last_name,
                    }
                )


            return JsonResponse({"status": "success", "message": "Users exported successfully."})

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method."}, status=400)