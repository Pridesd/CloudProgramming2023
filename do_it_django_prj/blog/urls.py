## urlconf for blog
from django.urls import path

from . import views #현재 위치에 있는 views를 가지고 옴

urlpatterns = [
    path('', views.index),
    path('<int:post_num>/', views.singlePostPage),
]