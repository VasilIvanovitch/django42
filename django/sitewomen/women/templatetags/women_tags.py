from django import template
from django.db.models import Count

import women.views as views
from women.models import Category, TagPosts

register = template.Library()


@register.simple_tag()
def get_categories():
    return views.cats_db


@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.alias(total=Count('womens')).filter(total__gt=0)
    return {'cats': cats, 'cat_selected': cat_selected}

@register.inclusion_tag('women/list_tags.html')
def show_all_tags():
    tags = TagPosts.objects.annotate(total=Count('womens')).filter(total__gt=0)
    return {'tags': tags}