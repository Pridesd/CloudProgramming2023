import os.path

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to= 'blog/images/%Y/%M/%D/' ,blank=True) #blank는 필수항목이 아니라는 뜻임 연월일 별로 폴더를 만들에서 제작함
    file_upload = models.FileField(upload_to= 'blog/files/%Y/%M/%D/' ,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]-{self.title}'
    def get_absolute_url(self):
        return f'/blog/{self.pk}'
    def get_file_name(self):
        return os.path.basename(self.file_upload.name) #파일 이름만 나타나게 하는 함수
