from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('loginsys.urls'), name="auth"),
    url(r'^', include('article.urls'), name="blog_articles")
]
