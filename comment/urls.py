from django.conf.urls import url, include
from .views import post_comment
app_name = 'comment'
urlpatterns = [
    url(r'^post_comment/(?P<pk>[0-9]+)/$', post_comment, name='post_comment'),
]