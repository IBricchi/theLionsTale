from django.conf.urls import url
from . import views

urlpatterns = [
    # author/
    url(r'^$', views.index, name='authorIndex'),
    # author/<int>
    url(r'^(?P<author_id>[0-9]+)/$', views.author, name='author'),

    url(r'^change/profile/pic/change$', views.profilePicChange, name='profilePicChange'),
    url(r'^change/profile/desc/change$', views.descChange, name='profileDescChange')
]