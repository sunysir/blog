from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from .views import PostView, CategoryView, ArchivesView, TagsView, IndexView
app_name = 'blog'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', login_required(PostView.as_view()), name='detail'),
    url(r'^category/(?P<pk>[0-9]+)/$', CategoryView.as_view(), name='category'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', ArchivesView.as_view(), name='archives'),
    url(r'^tags/(?P<pk>[0-9]+)/$', TagsView.as_view(), name='tags')

]