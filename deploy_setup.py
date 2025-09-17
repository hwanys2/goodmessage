#!/usr/bin/env python
"""
Railway 배포 후 실행되는 설정 스크립트
"""
import os
import django

# Django 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'goodmessage_project.settings')
django.setup()

from good_messages.models import Message
from django.contrib.auth.models import User

def setup_production():
    """프로덕션 환경 설정"""
    print("프로덕션 환경 설정을 시작합니다...")
    
    # 샘플 메시지 추가 (데이터베이스가 비어있는 경우)
    if not Message.objects.exists():
        print("샘플 메시지를 추가합니다...")
        
        # 학생들을 위한 긍정적인 메시지들
        sample_messages = [
            # 동기부여 메시지
            {"content": "오늘도 새로운 가능성이 가득한 하루입니다! 💫", "category": "동기부여"},
            {"content": "작은 노력도 모이면 큰 변화를 만들어냅니다. 🌱", "category": "동기부여"},
            {"content": "실패는 성공의 어머니입니다. 포기하지 마세요! 🌟", "category": "동기부여"},
            {"content": "꿈을 향해 한 걸음씩 나아가는 여러분이 자랑스럽습니다. 🚀", "category": "동기부여"},
            {"content": "오늘의 노력이 내일의 기적을 만듭니다! ✨", "category": "동기부여"},
            
            # 격려 메시지
            {"content": "여러분은 생각보다 훨씬 더 강하고 용감합니다! 💪", "category": "격려"},
            {"content": "힘들 때일수록 여러분의 진짜 실력이 나타납니다. 🔥", "category": "격려"},
            {"content": "어려운 길을 선택한 여러분, 정말 대단해요! 👏", "category": "격려"},
            {"content": "포기하고 싶을 때가 바로 한 번 더 해볼 때입니다! 💫", "category": "격려"},
            {"content": "여러분의 노력하는 모습이 아름답습니다. 🌸", "category": "격려"},
            
            # 학습 관련
            {"content": "공부는 미래의 나에게 주는 가장 소중한 선물입니다. 🎁", "category": "학습"},
            {"content": "모르는 것을 아는 것이 진정한 지혜의 시작입니다. 📚", "category": "학습"},
            {"content": "질문하는 것을 두려워하지 마세요. 그것이 성장의 열쇠입니다! 🔑", "category": "학습"},
            {"content": "오늘 배운 것이 내일의 힘이 됩니다. 📖", "category": "학습"},
            {"content": "천천히 가도 괜찮아요. 중요한 것은 멈추지 않는 것입니다! 🐢", "category": "학습"},
            
            # 우정과 협력
            {"content": "친구들과 함께하면 어떤 일도 즐거워집니다! 👫", "category": "우정"},
            {"content": "서로 도우며 함께 성장하는 것이 진정한 교육입니다. 🤝", "category": "우정"},
            {"content": "다양한 친구들과의 만남이 여러분을 더 풍요롭게 만듭니다. 🌈", "category": "우정"},
            {"content": "배려하는 마음이 가장 아름다운 인성입니다. 💝", "category": "우정"},
            {"content": "함께 웃고 함께 울 수 있는 친구가 있다는 것은 큰 행복입니다! 😊", "category": "우정"},
            
            # 자신감
            {"content": "여러분은 각자 특별하고 소중한 존재입니다! ⭐", "category": "자신감"},
            {"content": "자신을 믿는 것이 모든 성공의 첫 번째 비결입니다. 🌟", "category": "자신감"},
            {"content": "여러분만의 독특함이 세상을 더 아름답게 만듭니다. 🎨", "category": "자신감"},
            {"content": "완벽하지 않아도 괜찮아요. 그것이 바로 여러분의 매력입니다! 💖", "category": "자신감"},
            {"content": "오늘의 여러분도 충분히 멋지고 훌륭합니다! 👑", "category": "자신감"},
            
            # 감사와 행복
            {"content": "작은 것에도 감사할 줄 아는 마음이 행복의 비결입니다. 🙏", "category": "감사"},
            {"content": "오늘 하루도 건강하게 함께할 수 있어서 감사합니다! 💚", "category": "감사"},
            {"content": "웃음은 세상에서 가장 아름다운 언어입니다. 😄", "category": "행복"},
            {"content": "긍정적인 생각이 긍정적인 결과를 만들어냅니다! ☀️", "category": "행복"},
            {"content": "행복은 멀리 있지 않아요. 바로 지금 여기에 있습니다! 🌺", "category": "행복"},
        ]
        
        # 메시지 추가
        for msg_data in sample_messages:
            Message.objects.create(
                content=msg_data["content"],
                category=msg_data["category"],
                is_active=True
            )
        
        print(f"{len(sample_messages)}개의 샘플 메시지가 추가되었습니다!")
    else:
        print("이미 메시지가 존재합니다.")
    
    print("프로덕션 환경 설정이 완료되었습니다! 🎉")

if __name__ == "__main__":
    setup_production()
