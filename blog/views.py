from django.shortcuts import render, get_object_or_404
from .models import Article, Category

def home(request):
    context = {
        'articles' : Article.objects.published().order_by('-published')[:3]
    }
    return render(request, 'home.html', context)

def detail(request, slug):
    context = {
        'article' : get_object_or_404(Article.objects.published(), status = 'p', slug = slug)
    }
    return render(request, 'detail.html', context)

def category(request, slug):
    context = {
        'category' : get_object_or_404(Category, slug = slug)
    }
    return render(request, 'category.html', context)