from django.shortcuts import render, redirect, render_to_response
#회원가입과 로그인 폼을 불러옴
from django.views.decorators.csrf import csrf_exempt

from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout,
)

# 시작페이지
def home(request):
    # 로그인 하지 않은 상태
    if not request.user.is_authenticated:
        data = {"username": request.user,
                "is_authenticated": request.user.is_authenticated}
    # 로그인 한 상태
    else:
        data = {"last_login": request.user.last_login,
                "username": request.user.username,
                "password": request.user.password,
                "is_authenticated": request.user.is_authenticated}
    return render(request, 'blog/index.html', context={"data": data}) #context: templates전달

#회원가입 페이지
@csrf_exempt
def join(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        # 입력값에 문제가 없으면(모든 유효성 검증 규칙을 통과 할 때)
        if form.is_valid():
            #form.cleaned_data
            #검증에 성공한 값들을 딕셔너리 타입으로 저장하고 있는 데이터
            #새로운 사용자가 생성됨
            new_user =\
                User.objects.create_user(**form.cleaned_data) # **keyword qrgument :키워드 인자 (위치가 중요한 게 아니라 이름으로 호출)
            #로그인 처리
            django_login(request, new_user)
            #시작페이지로 이동
            return redirect("/")
        else: #중복 아이디, 비밀번호 규칙 안 맞음
            return render_to_response("blog/index.html", {"msg": "회원가입 실패! 다시 시도해보세요"})
    else: #get방식
        #post방식이 아닌 경우 회원가입 페이지로 이동
        form = UserForm()
        return render(request, "blog/join.html", {"form": form})
    return render(request, "blog/index.html")



def logout(request):
    #django에 내장된 로그아웃 처리 함수
    django_logout(request)
    #시작페이지로 이동
    return redirect("/")

def login_check(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        name = request.POST["username"]
        pwd = request.POST["password"]
        user = authenticate(username=name, password=pwd)
        if user is not None:  # 로그인 성공
            django_login(request, user)
            return redirect("/")
        else:  # 로그인 실패
            return render_to_response("blog/index.html", {"msg": "로그인 실패! 다시 시도해 보세요"})
    else: #get방식
        #post방식이 아닌 경우 회원가입 페이지로 이동
        form = LoginForm()
        return render(request, "blog/login.html", {"form": form})