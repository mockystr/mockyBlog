from django.contrib import admin
from .models import Article, Comment


class ArticleInline(admin.StackedInline):
    model = Comment
    extra = 2


class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_date']
    inlines = [ArticleInline]
    list_filter = ['article_date']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
