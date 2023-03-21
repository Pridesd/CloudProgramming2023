from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-pk') #-를 붙이면 내림차순으로 정렬
    return render(
        request,
        'blog/index.html', #자동으로 templates로 연결됨
        {
            'posts': posts
        }
    )
def singlePostPage(request, post_num):
    post = Post.objects.get(pk = post_num)

    return render(
        request,
        'blog/singlePostPage.html',
        {
            'post': post
        }
    )