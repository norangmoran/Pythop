from django.urls import path
from . import views # 현재 폴더의 views를 가져옴

urlpatterns = [
    path('', views.index), #views.py에 index 함수
]