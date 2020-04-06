# 4월 6일 exercise

### 1.  views.py

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
    title = request.GET.get('title')
    content = request.GET.get('content')

    article = Article()
    article.title = title
    article.content = content
    article.save()

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
        'article': article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(id=pk)
    article.title=request.GET.get('title')
    article.content=request.GET.get('content')
    article.save()
    return redirect(f'/articles/{article.pk}/')

def delete(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()
    return redirect('/articles/')
```

### 2. articles/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:pk>/', views.detail),
    path('<int:pk>/edit/', views.edit),
    path('<int:pk>/delete/', views.delete),
    path('<int:pk>/update/', views.update),
    ]
```

### 3. articles/models.py

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### 4. base.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Exercise 0406</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
</head>
<body>
    {% block content %}
    {% endblock %}
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>
```

### 5. index.html

```html
{% extends 'base.html' %}

{% block content %}
    <h1>INDEX</h1>
    <a href="/articles/new">NEW</a>
    <hr>
    {% for article in articles %}
    <br>
    <h3>제목: {{ article.title }}</h3>
    <p>내용: {{ article.content }}</p>
    <a href="/articles/{{ article.pk }}">Detail</a>
    <br>
    {% endfor %}
{% endblock %}
```

![](C:\TurtleLab\SSAFY\online-lectures(과제업로드)\0406\exercise\images\index.PNG)

---

### 6. new.html (+create)

```html
{% extends 'base.html' %}

{% block content %}
    <h1>NEW</h1>
    <hr>
    <form action='/articles/create/' method="GET">
        <h3>title : <input type='text' id='title' name='title'></h3>
        <p>content : <textarea id='content' name='content'> </textarea></p>
        <input type='submit'><br>
        <a href="/articles/">Back</a>
    </form>
{% endblock %}
```

![](C:\TurtleLab\SSAFY\online-lectures(과제업로드)\0406\exercise\images\new.PNG)

---

### 7. detail.html

```html
{% extends 'base.html' %}

{% block content %}
<h1>Detail</h1>
<hr>
<h2>{{ article.title }}</h2>
<p>{{ article.content }}</p>
<p>작성일 : {{ article.created_at }}</p>
<p>수정일 : {{ article.updated_at }}</p>
<a href="/articles/{{ article.pk }}/edit">Edit</a>
<a href="/articles/{{ article.pk }}/delete">Delete</a><br>
<a href="/articles/">Back</a>
{% endblock %}
```

![](C:\TurtleLab\SSAFY\online-lectures(과제업로드)\0406\exercise\images\detail.PNG)

---

### 8. edit.html(+delete, update)

```html
{% extends 'base.html' %}

{% block content %}
<h1>EDIT</h1>
<hr>
<form action="/articles/{{ article.pk }}/update/" method=GET>
    제목: <input type="text" name="title" id='title' value="{{ article.title }}"><br>
    내용: <textarea name='content' id='content' value="{{ article.content }}">{{ article.content }}</textarea><br>
    <input type="submit"><br>
    <a href="/articles/{{ article.pk }}/">Back</a>
</form>
{% endblock %}
```

![](C:\TurtleLab\SSAFY\online-lectures(과제업로드)\0406\exercise\images\edit.PNG)
