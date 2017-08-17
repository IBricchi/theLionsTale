from django.conf.urls import url
from . import views

urlpatterns = [
    # article/
    url(r'^$', views.index, name="articleIndex"),
    # article/<int>
    url(r'^(?P<article_id>[0-9]+)/$', views.article, name='article'),
    # article/upload/<int>
    url(r'^upload/(?P<user_key>[0-9]+)/$', views.uploadDisp, name='upload'),
    # article/upload/<int>/post
    url(r'^upload/(?P<user_key>[0-9]+)/post/$', views.upload, name='post')
]
