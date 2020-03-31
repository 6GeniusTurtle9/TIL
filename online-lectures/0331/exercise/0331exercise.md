# 3월 31일 exercise

* 결과 사진(ping)

  ![](C:\TurtleLab\SSAFY\online-lectures(과제업로드)\0331\exercise\images\ex1.PNG)

* 결과 사진(pong)

![](C:\TurtleLab\SSAFY\online-lectures(과제업로드)\0331\exercise\images\ex2.PNG)

### 1.  views.py

```python
from django.shortcuts import render

# Create your views here.
def ping(request):
    return render(request, 'articles/ping.html')

def pong(request):
    search_data = request.GET.get('search_data')
    context = {
        'search_data':search_data
    }
    return render(request, 'articles/pong.html',context)
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
    path('ping/', views.ping),
    path('pong/', views.pong),
    ]
```



### 4. base.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>0331Exercise</title>
</head>
<body>
    {% block content %}
    {% endblock %}
</body>
</html>
```



### 5. ping.html

```html
{% extends 'base.html' %}

{% block content %}
    <h1>여기는 ping</h1>
    <h2>pong으로 데이터를 보내보자!</h2>
    <form action="/articles/pong/" method='GET'>
        <input type="text" name=search_data>
        <input type='submit'>
    </form>
{% endblock %}
```



### 6. pong.html

```html
{% extends 'base.html' %}

{% block content %}
    <h1>여기는 pong</h1>
    <h2>ping에서 {{ search_data }}를 받았어!</h2>
{% endblock %}
```



