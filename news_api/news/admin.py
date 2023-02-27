from django.contrib import admin

from . models import Category, Author, Tag, News


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'create_at']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'avatar', 'position', 'bio']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'create_at']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in News._meta.get_fields() if not field.many_to_many]
