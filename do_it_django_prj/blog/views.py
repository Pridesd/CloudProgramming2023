from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-pk') #-를 붙이면 내림차순으로 정렬
    return render(
        request,
        'blog/index.html',
        {
            'posts': posts
        }
    )