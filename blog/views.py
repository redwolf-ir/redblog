from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from django.core.paginator import Paginator


def home(request, page = 1):
    article_list = Article.objects.published()
    paginator = Paginator(article_list, 1)
    articles = paginator.get_page(page)
    context = {
        'articles' : articles,
    }
    return render(request, 'home.html', context)

def detail(request, slug):
    context = {
        'article' : get_object_or_404(Article.objects.published(), status = 'p', slug = slug)
    }
    return render(request, 'detail.html', context)

def category(request, slug, page = 1):
    category = get_object_or_404(Category, slug = slug)
    article_list = category.articles.published()
    paginator = Paginator(article_list, 1)
    articles = paginator.get_page(page)
    context = {
        'category' : category,
        'articles' : articles,
    }
    return render(request, 'category.html', context)