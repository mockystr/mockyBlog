from django import template

register = template.Library()


@register.filter(name='reverse_last_five')
def reverse_last_five(value):
    return value[len(value) - 5:]