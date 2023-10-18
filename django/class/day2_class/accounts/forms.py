from django import forms
from django.contrib.auth.forms import UserCreationForm
# Django 공식 문서에서 권장하지 않는다고 명시되어 있음
# from .models import User

from django.contrib.auth import get_user_model

# Django가 제공하는 CreationForm을 상속받아서
# 우리가 정의한 User 모델을 사용하도록 새로 생성

class CustomCreationForm(UserCreationForm):
    # 추가할 필드 정의
    nickname = forms.CharField(max_length=30, required=False, help_text="필요 시 닉네임 지정하세요")
    class Meta(UserCreationForm.Meta):
        # get_user_model(): 현재 프로젝트에 세팅된 User 모델을 가져오는 역할
        model = get_user_model()
        # 앞으로 사용할 field는 기존 것 + nickname 필드이다.
        fields = UserCreationForm.Meta.fields + ('nickname', )