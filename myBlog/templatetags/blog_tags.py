from django import template
from django.db.models import Count

from ..models import Category, Post, Tag
register = template.Library()
@register.simple_tag
def get_category():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
@register.simple_tag
def get_archives():
    return Post.objects.dates('created_time', 'month', order='DESC')