from django.shortcuts import render
from .models import Article

def home(request):
    context = {
        'articles' : Article.objects.filter(status = 'p').order_by('-published')[:3]
    }
    return render(request, 'home.html', context)