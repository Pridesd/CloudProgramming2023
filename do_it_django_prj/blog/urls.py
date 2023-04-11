## urlconf for blog
from django.urls import path

from . import views #현재 위치에 있는 views를 가지고 옴

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('category/<str:slug>', views.categories_page),
    path('tag/<str:slug>', views.tag_page),
    path('create_post/', views.PostCreate.as_view()),
]