from django import template

register = template.Library()


@register.filter(name='reverse_last_five')
def reverse_last_five(value):
    return value[len(value) - 5:]


@register.filter(name='reverse_all')
def reverse_all(value):
    return value[::-1]
