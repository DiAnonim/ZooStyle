from django import template

register = template.Library()

@register.filter
def isHaveValue(value):
    return value if value else "-"