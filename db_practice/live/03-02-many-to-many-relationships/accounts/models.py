from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')# 중개테이블을 만들기 때문에 기존 유저 테이블에는 변화가 없음