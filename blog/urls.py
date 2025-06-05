from django.urls import path
from . import views # 현재 폴더의 views를 가져옴

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.single_post_page),
    # path('', views.index), #views.py에 index 함수
]
