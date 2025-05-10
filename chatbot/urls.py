from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot_view, name='chatbot'),
    path('get-response/', views.get_response, name='get_response'),
]
