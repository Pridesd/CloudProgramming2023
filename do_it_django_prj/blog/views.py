from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.

# def index(request):
#     posts = Post.objects.all().order_by('-pk') #-를 붙이면 내림차순으로 정렬
#     return render(
#         request,
#         'blog/post_list.html', #자동으로 templates로 연결됨
#         {
#             'posts': posts
#         }
#     )
# def singlePostPage(request, post_num):
#     post = Post.objects.get(pk = post_num)
#
#     return render(
#         request,
#         'blog/post_detail.html',
#         {
#             'post': post
#         }
#     )
class PostList(ListView):
    model = Post
    ordering = '-pk'
class PostDetail(DetailView):
    model = Post
