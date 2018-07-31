from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^article/(?P<article_id>\d+)/$', views.article, name="post"),
    url(r'^article/addlike/(?P<article_id>\d+)/$', views.addlike, name="like"),
    url(r'^article/addcomment/(?P<article_id>\d+)/$', views.addcomment, name="comment"),
    url(r'^find/(\d+)/$', views.find_article, name="find"),
    url(r'^page/(\d+)/$', views.articles, name="post_with_pages"),
    url(r'^$', views.articles),
]
