# Generated by Django 4.1.5 on 2023-02-27 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_author_news_image_alter_news_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='author',
        ),
        migrations.RemoveField(
            model_name='news',
            name='tag',
        ),
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.ManyToManyField(blank=True, null=True, related_name='news_author', to='news.author'),
        ),
        migrations.AddField(
            model_name='news',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, related_name='news_tag', to='news.tag'),
        ),
    ]