from django.contrib import admin

from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'create_at']


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'avatar', 'position', 'bio']


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'create_at']


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'content', 'create_at', 'category', 'author', 'tag']
