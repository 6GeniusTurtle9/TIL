from django.shortcuts import render
from .models import Article

# Create your views here.
def ping(request):
    return render(request, 'ping.html')

def pong(request):
    ping = request.GET.get('ping')
    context = {
        'ping':ping
    }
    return render(request, 'pong.html', context)


def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    #1. 사용자 입력 데이터 가져오기
    title = request.GET.get('title')
    contenet = request.GET.get('content')

    #2. DB 저장
    article = Article(title=title, content=content)
    article.save()

    return render(request, 'articles/create.html')