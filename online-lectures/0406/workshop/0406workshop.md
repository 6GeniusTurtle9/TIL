# 4월 6일 workshop

### 1. articles/urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    ]
```



### 2. index.html

```html
{% extends 'base.html' %}

{% block content %}
    <h1>INDEX</h1>
    <a href='{% url 'articles:new' %}'>NEW</a>
    <hr>
    {% for article in articles %}
    <br>
    <h3>제목: {{ article.title }}</h3>
    <p>내용: {{ article.content }}</p>
    <a href="{% url 'articles:detail' article.pk %}">Detail</a>
    <br>
    {% endfor %}
{% endblock %}
```



### 3. new.html

```html
{% extends 'base.html' %}

{% block content %}
    <h1>NEW</h1>
    <hr>
    <form action='{% url 'articles:create' %}' method="POST">{% csrf_token %}
        <h3>title : <input type='text' id='title' name='title'></h3>
        <p>content : <textarea id='content' name='content'> </textarea></p>
        <input type='submit'><br>
        <a href="{% url 'articles:index' %}">Back</a>
    </form>
{% endblock %}
```



### 4. detail.html

```html
{% extends 'base.html' %}

{% block content %}
<h1>Detail</h1>
<hr>
<h2>{{ article.title }}</h2>
<p>{{ article.content }}</p>
<p>작성일 : {{ article.created_at }}</p>
<p>수정일 : {{ article.updated_at }}</p>
<a href="{% url 'articles:edit' article.pk %}">Edit</a>
<a href="{% url 'articles:delete' article.pk %}">Delete</a><br>
<a href="{% url 'articles:index' %}">Back</a>
{% endblock %}
```



### 5. edit.html

```html
{% extends 'base.html' %}

{% block content %}
<h1>EDIT</h1>
<hr>
<form action="{% url 'articles:update' article.pk %}" method="POST">{% csrf_token %}
    제목: <input type="text" name="title" id='title' value="{{ article.title }}"><br>
    내용: <textarea name='content' id='content' value="{{ article.content }}">{{ article.content }}</textarea><br>
    <input type="submit"><br>
    <a href="{% url 'articles:detail' article.pk %}">Back</a>
</form>
{% endblock %}
```



### 6. views.py

```python
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
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article()
    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', article.pk)

def detail(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        'article': article
    }
    return render(request,'articles/detail.html', context)

def edit(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(id=pk)
    article.title=request.POST.get('title')
    article.content=request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)

def delete(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()
    return redirect('articles:index')
```

