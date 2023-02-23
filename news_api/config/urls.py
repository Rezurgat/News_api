from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from news import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'news', views.NewsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

