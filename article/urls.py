from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [
    url(r'^article/(?P<article_id>\d+)/$', views.article, name="post"),
    url(r'^article/addlike/(?P<article_id>\d+)/$', views.addlike, name="like"),
    url(r'^article/addcomment/(?P<article_id>\d+)/$', views.addcomment, name="comment"),
    url(r'^find/(\d+)/$', views.find_article, name="find"),
    url(r'^page/(\d+)/$', views.articles, name="post_with_pages"),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^$', views.articles),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += staticfiles_urlpatterns()
