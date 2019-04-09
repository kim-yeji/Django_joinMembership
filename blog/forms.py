from django import forms
from django.contrib.auth.models import User  # 인증 관련 주요 모델필드

# 회원가입 폼
class UserForm(forms.ModelForm):
    class Meta:
        # 사용자 정보를 저장하는 클래스
        model = User
        # 회원가입 폼에 표시될 필드
        fields = ["username", "email", "password"]


# 로그인 폼
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
