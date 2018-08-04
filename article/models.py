# coding: utf-8
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    class Meta:
        db_table = "Article"

    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateTimeField(null=True)
    article_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.article_title


class Comment(models.Model):
    class Meta:
        db_table = "Comment"

    comments_text = models.TextField(verbose_name="Текст комментария")
    comments_article = models.ForeignKey('Article')
    comments_date = models.DateField(u'date', auto_now=True)
    comments_author = models.ForeignKey(User, default=9)

    def __str__(self):
        return self.comments_text + " --> " + self.comments_article.article_title
