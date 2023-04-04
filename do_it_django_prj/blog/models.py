import os.path
from django.contrib.auth.models import User

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    hook = models.CharField(max_length=30, blank=True)

    head_image = models.ImageField(upload_to='blog/images/%Y/%M/%D/',blank=True) #blank는 필수항목이 아니라는 뜻임 연월일 별로 폴더를 만들에서 제작함
    file_upload = models.FileField(upload_to='blog/files/%Y/%M/%D/',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #author가 없어지면 게시글도 삭제

    def __str__(self):
        return f'[{self.pk}]-{self.title} - {self.author}'
    def get_absolute_url(self):
        return f'/blog/{self.pk}'
    def get_file_name(self):
        return os.path.basename(self.file_upload.name) #파일 이름만 나타나게 하는 함수
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True) #유일한 값을 가져야함
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)
    #유니코드(한글)의 사용도 가능케 함
    # 슬러그는 키워드를 나타냄 읽을 수 있는 텍스트로 URL로 만들 때 사용
    
    #카테고리 이름을 찾아오게끔 함
    def __str__(self):
        return self.name
