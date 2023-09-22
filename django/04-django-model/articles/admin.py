from django.contrib import admin
# 명시적 상대경로 (Django에서는 작성하는게 좋다)
from .models import Article
# Register your models here.

# Article 모델 클래스를 admin site에 등록
# admin site에 등록한다고 외우면 됨
admin.site.register(Article)