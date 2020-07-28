from django.shortcuts import render, get_object_or_404
from .models import Article

def home(request):
    context = {
        'articles' : Article.objects.filter(status = 'p').order_by('-published')[:3]
    }
    return render(request, 'home.html', context)

def detail(request, slug):
    context = {
        'article' : get_object_or_404(Article, status = 'p', slug = slug)
    }
    return render(request, 'detail.html', context)