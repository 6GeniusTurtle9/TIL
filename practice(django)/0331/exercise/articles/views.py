from django.shortcuts import render
from .models import Article

# Create your views here.
def ping(request):
    return render(request, '/ping.html')

def pong(request):
    search_data = request.GET.get('search')
    context = {
        'search_data': search_data
    }
    return render(request, 'pong.html', context)

def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
        #'articles':[1, 2, 3]
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')


def create(request):
    article = Article()
    article.title = request.GET.get('title')
    article.content = request.GET.get('content')
    article.save()
    return render(request, 'articles/create.hhtml')

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)
