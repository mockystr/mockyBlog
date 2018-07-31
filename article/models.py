# coding: utf-8
from django.db import models


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

    def __str__(self):
        return self.comments_text + " --> " + self.comments_article.article_title
