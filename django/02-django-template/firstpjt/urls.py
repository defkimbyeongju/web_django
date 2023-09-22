"""
URL configuration for firstpjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from articles import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # # 1번 실습 변수
    # path('articles/', views.index),
    # # 2번 실습 DTL
    # path('dinner/', views.dinner),
    # # 3번 실습 form 태그
    # path('search/', views.search),
    # # 4번 실습 throw, catch
    # path('throw/', views.throw),
    # path('catch/', views.catch),
    # path('hello/<str:name>/', views.greeting),
    # path('articles/<int:num>/', views.detail),
    path('articles/', include('articles.urls')),
    # path('pages/', include('pages.urls')),
]
