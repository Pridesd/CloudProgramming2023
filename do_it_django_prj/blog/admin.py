from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Post, Category, Tag

admin.site.register(Post, MarkdownxModelAdmin)
#카테고리의 슬러그가 이름에 대해 자동 기입이 되기 위함
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
admin.site.register(Tag, TagAdmin)
