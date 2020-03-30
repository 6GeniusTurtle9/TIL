# 3월 30일 exercise

* 결과 사진

  ![](C:\TurtleLab\SSAFY\online-lectures(과제업로드)\0330\exercise\images\exer1.PNG)

![](C:\TurtleLab\SSAFY\online-lectures(과제업로드)\0330\exercise\images\exer2.PNG)

### 1.  intro/settings.py

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'intro', 'templates')],
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



### 2. intro/urls.py

```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('card/', 'views.card'),
    path('community/', 'views.community'),
]
```



### 3. pages/view.py

```python
from django.shortcuts import render

# Create your views here.
def card(request):
    articles = [
        ['test title1', 'test content1'],
        ['test title2', 'test content2'],
        ['test title3', 'test content3'],
        ['test title4', 'test content4'],
        ['test title5', 'test content5'],
    ]
    context = {
        'articles': articles
    }
    return render(request, 'card.html', context)

def community(request):
    articles = [
        ['#', 'Title', 'Content', 'Creation Time'],
        ['test title 1', 'test content 1', 'test creation time1'],
        ['test title 2', 'test content 2', 'test creation time2'],
        ['test title 3', 'test content 3', 'test creation time3'],
        ['test title 4', 'test content 4', 'test creation time4'],
        ['test title 5', 'test content 5', 'test creation time5'],
        ['test title 6', 'test content 6', 'test creation time6'],
    ]
    context = {
        'articles': articles
    }
    return render(request, 'community.html', context)
```



### 4. intro/templates/base.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>0330exercise</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">Article</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link" href="/card/">Card</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/community/">Community</a>
          </li>
       </div>
    </nav>
    <div class="container">
    {% block content %}
    {% endblock %}
    </div>
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>
```



### 5. pages/templates/card.html

```html
{% extends 'base.html' %}

{% block content %}

<div class="row">
{% for article in articles %}
    <div class="card" style="width: 18rem;">
      <img class="card-img-top" src="https://i.picsum.photos/id/212/200/300.jpg" alt="Card image cap">
      <div class="card-body">
        <h5 class="card-title">{{ article.0 }}</h5>
        <p class="card-text">{{ article.1 }}</p>
        <a href="/community/" class="btn btn-primary">Post Article</a>
      </div>
    </div>
{% endfor %}
</div>
{% endblock %}
```



### 6. pages/templates/community.html

```html
{% extends 'base.html' %}

{% block content %}

<table class="table">
    <thead class="thead-dark">
    <tr>
        <th scope="col">{{ articles.0.0 }}</th>
        <th scope="col">{{ articles.0.1 }}</th>
        <th scope="col">{{ articles.0.2 }}</th>
        <th scope="col">{{ articles.0.3 }}</th>
    </tr>
    </thead>
    <tbody>
    {% for article in articles %}
        {% if forloop.counter0 > 0 %}
        <tr>
            <th scope="row">{{ forloop.counter0 }}</th>
            <td>{{ article.0 }}</td>
            <td>{{ article.1 }}</td>
             <td>{{ article.2 }}</td>
        </tr>
        {% endif %}
    {% endfor %}
    </tbody>
</table>
{% endblock %}
```



