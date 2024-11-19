import os
import subprocess
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def runMLScript(request):
    script_path = os.path.join('Backend', 'Text_Preprocessing', 'example_script.py')

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
    return render(request, "index.html", context)
