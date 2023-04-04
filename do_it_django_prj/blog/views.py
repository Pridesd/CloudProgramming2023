from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post, Category

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

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None)

        return context
class PostDetail(DetailView):
    model = Post


def categories_page(request, slug):
    if slug == "no-category":
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)
    context = {
        'category': category,
        'categories': Category.objects.all(),
        'post_list': post_list,
    }
    return render(
        request,
        'blog/post_list.html',
        context
    )