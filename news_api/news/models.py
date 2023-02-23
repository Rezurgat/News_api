from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', null=True)
    position = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    class Meta:
        ordering = ['firstname']


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class News(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='news_media/', null=True)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='news_category', on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Author, related_name='news_author', on_delete=models.SET_DEFAULT, null=True, default='Null')
    tag = models.ForeignKey(Tag, related_name='news_tag', on_delete=models.SET_DEFAULT, null=True, default='Null')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['create_at']

    def get_category_name(self):
        return self.category.name

    def get_category_slug(self):
        return self.category.slug









