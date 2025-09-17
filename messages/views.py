from django.shortcuts import render
from django.http import JsonResponse
from .models import Message
import random

def home(request):
    """메인 페이지 - 랜덤 메시지 표시"""
    # 활성화된 메시지 중에서 랜덤하게 선택
    active_messages = Message.objects.filter(is_active=True)
    
    if active_messages.exists():
        random_message = random.choice(active_messages)
        message_content = random_message.content
        message_category = random_message.category
    else:
        message_content = "오늘도 좋은 하루 보내세요! 😊"
        message_category = "기본"
    
    context = {
        'message': message_content,
        'category': message_category,
    }
    
    return render(request, 'messages/home.html', context)

def get_random_message(request):
    """AJAX용 랜덤 메시지 API"""
    active_messages = Message.objects.filter(is_active=True)
    
    if active_messages.exists():
        random_message = random.choice(active_messages)
        data = {
            'message': random_message.content,
            'category': random_message.category,
        }
    else:
        data = {
            'message': "오늘도 좋은 하루 보내세요! 😊",
            'category': "기본",
        }
    
    return JsonResponse(data)
