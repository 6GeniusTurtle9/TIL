# 3월 31일 workshop

### 1. crud/settings.py

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'crud', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```



### 2. crud/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls'))
]
```



### 3. articles/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    
    ]
```

### 4. articles/views.py

```python
from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):

    title = request.GET.get('title')
    content = request.GET.get('content')

    articles = Article(title=title, content=content)
    articles.save()

    return render(request, 'articles/create.html')
```



### 5. crud/templates/base.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Workshop 0331</title>
</head>
<body>
    <h1>Articles</h1>
    <hr>
    {% block content %}

    {% endblock %}
</body>
</html>
```

![](C:\TurtleLab\SSAFY\online-lectures(과제업로드)\0331\workshop\images\base.PNG)

### 6. templates/articles/index.html

```html
{% extends 'base.html' %}

{% block content %}
<a href="/articles/new/">NEW</a>
<h2>게시글 모음</h2>
{% for article in articles %}
    <h3>제목 : {{ article.title }}</h3>
    <p>내용 : {{ article.content }}<p>
{% endfor %}
{% endblock %}
```

![](C:\TurtleLab\SSAFY\online-lectures(과제업로드)\0331\workshop\images\index.PNG)

### 7. templates/articles/new.html

```html
{% extends 'base.html' %}

{% block content %}
    <h2>글작성</h2>
    <form action="/articles/create/" method="GET">
        <h3>제목 : <input type="text" name="title" id='title'></h3>
        <h3>내용 : <input type="text" name="content" id='content'></h3>
        <input type="submit">
    </form>
    <hr>
    <a href="/articles/">BACK</a>
{% endblock %}
```

![](C:\TurtleLab\SSAFY\online-lectures(과제업로드)\0331\workshop\images\new.PNG)

### 8. templates/articles/create.html

```html
{% extends 'base.html' %}

{% block content %}
    <h2>성공적으로 글이 작성되었습니다.</h2>

    <a href="/articles/">BACK</a>
{% endblock %}
```

![](C:\TurtleLab\SSAFY\online-lectures(과제업로드)\0331\workshop\images\create.PNG)

