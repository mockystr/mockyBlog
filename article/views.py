from django.shortcuts import render, redirect
from .models import Article, Comment
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from .forms import CommentForm
from django.template.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator
from django.contrib.auth.models import User


def articles(request, page_number=1):
    all_articles = Article.objects.all()[::-1]
    current_page = Paginator(all_articles, 3)

    return render(request, template_name='article/articles.html',
                  context={
                      'articles': current_page.page(page_number),
                      'user': auth.get_user(request),
                      'cookies': request.COOKIES
                  })


def article(request, article_id=1):
    comment_form = CommentForm
    args = {}

    args.update(csrf(request))

    args["article"] = Article.objects.get(pk=article_id)
    args["comments"] = Comment.objects.filter(comments_article=article_id)
    args["rev_comments"] = args["comments"][::-1]
    args["user"] = auth.get_user(request)
    args["form"] = comment_form

    return render(request, 'article/article.html', args)


def addlike(request, article_id):
    try:
        if article_id in request.COOKIES:
            article_obj = Article.objects.get(id=article_id)
            article_obj.article_likes -= 1
            article_obj.save()

            responce = redirect(request.META.get('HTTP_REFERER'))
            responce.delete_cookie(article_id)
            return responce
        else:
            article_obj = Article.objects.get(id=article_id)
            article_obj.article_likes += 1

            article_obj.save()
            responce = redirect(request.META.get('HTTP_REFERER'))
            responce.set_cookie(article_id, 'likes')
            return responce
    except ObjectDoesNotExist:
        raise Http404
    return redirect(request.META.get('HTTP_REFERER'))


def addcomment(request, article_id):
    if request.POST:
        comment = request.POST.get("comment", "")
        if comment:
            comments_article = Article.objects.get(id=article_id)
            comments_author = request.user
            comment_insert = Comment(comments_text=comment, comments_article=comments_article,
                                     comments_author=comments_author)

            comment_insert.save()
        return redirect('/article/%s/' % article_id)


def find_article(request, page_number=1):
    if request.GET:
        if 'q' in request.GET:
            q = request.GET['q']
            all_search_res = Article.objects.all().filter(article_title__contains=q)[::-1]
            current_page = Paginator(all_search_res, 3)
            context = {
                'articles': Article.objects.all(),
                'user': auth.get_user(request),
                "search_res": current_page.page(page_number),
                'q': q
            }
            if len(context['search_res']) == 0:
                return redirect("/")
            else:
                return render(request, 'article/articles.html', context)
        else:
            raise Http404
    return redirect("/")
