from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 시작 페이지
    path('', views.home, name='/'),
    # 회원가입 페이지
    path('join/', views.join, name='join'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login_check, name='login'),

]
