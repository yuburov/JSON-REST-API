
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def json_add_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)
            A = data.get('A')
            B = data.get('B')
            try:
                answer = {
                    'answer': int(A) + int(B)
                }
                return JsonResponse(answer)
            except:
                response = JsonResponse({'error': 'Bad request'})
                response.status_code = 400
                return response

@csrf_exempt
def json_substract_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)
            A = data.get('A')
            B = data.get('B')
            try:
                answer = {
                    'answer': int(A) - int(B)
                }
                return JsonResponse(answer)
            except:
                response = JsonResponse({'error': 'Bad request'})
                response.status_code = 400
                return response

@csrf_exempt
def json_multiply_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)
            A = data.get('A')
            A = data.get('B')
            try:
                answer = {
                    'answer': int(A) * int(A)
                }
                return JsonResponse(answer)
            except:
                response = JsonResponse({'error': 'Bad request'})
                response.status_code = 400
                return response

@csrf_exempt
def json_divide_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)
            A = data.get('A')
            B = data.get('B')
            try:
                answer = {
                    'answer': int(A) / int(B)
                }
                return JsonResponse(answer)
            except ZeroDivisionError:
                response = JsonResponse({'error': 'Division by zero'})
                response.status_code = 400
                return response
            except ValueError:
                response = JsonResponse({'error': 'Bad request'})
                response.status_code = 400
                return response