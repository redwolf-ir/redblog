from django import template
from ..models import Category

register = template.Library()

@register.simple_tag
def title():
    return "وبلاگ جنگویی"

@register.inclusion_tag('nav.html')
def category_nav():
    return {
        "categories" : Category.objects.all()
    }