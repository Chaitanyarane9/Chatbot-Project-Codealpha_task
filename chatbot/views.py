from django.shortcuts import render
from django.http import JsonResponse
from .chatbot_engine import get_bot_response

def chatbot_view(request):
    return render(request, 'chatbot/chat.html')

def get_response(request):
    user_input = request.GET.get('msg')
    return JsonResponse({'response': get_bot_response(user_input)})
