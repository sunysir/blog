from django.contrib import admin
from .models import Tag, Post, Category

# Register your models here.
class PostShow(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time','category']
class TagShow(admin.ModelAdmin):
    list_display = ['name', ]
class CategoryShow(admin.ModelAdmin):
    list_display = ['name', ]
admin.site.register(Tag,TagShow)
admin.site.register(Post, PostShow)
admin.site.register(Category,CategoryShow)
