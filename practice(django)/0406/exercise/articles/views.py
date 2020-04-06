from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    #1. 데이터 가져오기
    title = request.GET.get('title')
    content = request.GET.get('content')

    #2. 데이터 저장
    article = Article()
    article.title = title
    article.content = content
    article.save()

    #3. Redirect
    return redirect('/articles/')

def detail(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        'article': article
    }
    return render(request,'articles/detail.html', context)

def edit(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        'articles': article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(id=pk)
    article.title=request.GET.get('title')
    article.content=request.GET.get('content')
    article.save()
    return redirect(f'/articles/{article.pk}/)

def delete(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()
    return redirect('/articles/')