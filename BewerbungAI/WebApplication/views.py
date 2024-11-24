import os
import subprocess

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def runMLScript(request):
    script_path = os.path.join('WebApplication', 'Text_Preprocessing', 'ml_code.py')

    try:
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        output = result.stdout
        error = result.stderr
    except Exception as e:
        output = f"Error occurred: {str(e)}"
        error = None

    context = {
        'output': output,
        'error': error
    }
    return JsonResponse(context)


def helloWorldScript(request):
    script_path = os.path.join('WebApplication', 'Text_Preprocessing', 'hello_world.py')

    try:
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        output = result.stdout
        error = result.stderr
    except Exception as e:
        output = f"Error occurred: {str(e)}"
        error = None

    context = {
        'output': output,
        'error': error
    }
    return JsonResponse(context)

