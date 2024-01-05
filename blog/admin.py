from django.contrib import admin
from .models import Category, Post, BlogImage


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_posted']

@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    list_display = ['post', 'image']

admin.site.register(Category)
