from django import template
from ..models import Comment

register = template.Library()


@register.filter(name='reverse_last_five')
def reverse_last_five(value):
    return value[len(value) - 5:]


@register.filter(name='reverse_all')
def reverse_all(value):
    return value[::-1]


@register.filter(name='get_comments_length')
def get_comments_length(value):
    obj = len(Comment.objects.filter(comments_article=value))
    return obj


@register.filter(name='format_str')
def format_str(value, username):
    return "{0}:{1}".format(value, username)


@register.filter(name='is_liked')
def is_liked(value, cookies_val):
    return True if str(value) in cookies_val else False
