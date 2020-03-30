# 3월 30일 workshop

### 1. urls.py

```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
]
```



### 2. views.py

```python
import requests
from pprint import pprint
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
```



### 3. index.html

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>고화질 이미지 생성기</h1>
    <h2>원하는 카테고리를 입력하세요!</h2>
    <form action="/pages/gallery/">
        <input type="text" name='search'>
        <input type="submit" value="조회하기">
    </form>
</body>
</html>
```

![](C:\TurtleLab\SSAFY\online-lectures(과제업로드)\0330\workshop\images\캡처1.PNG)

### 4. urls.py

```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('gallery/', views.gallery),
]
```



### 5. view.py

```python
import requests
from pprint import pprint
from django.shortcuts import render

def gallery(request):
    #1. 사용자 입력값 받기
    search_data = request.GET.get('search')

    #2. API 요청 보내기 -> (기본) API URL, Access Key / (사진검색) query
    client_id = '-CHdV0gwtxGK1gLf-prWxjw97QfJyfsVLAz2IQnk45Y'
    photo_url = f'https://api.unsplash.com/search/photos?client_id={client_id}&query={search_data}'
    response = requests.get(photo_url).json()

    #3. 응답값 확인 및 사진 추출
    photo_list = []

    for photo in response.get('results'):
        photo_list.append(photo.get('urls').get('regular'))

    context = {
        'photo_list': photo_list
    }

    return render(request, 'gallery.html', context)
```



### 6. gallery.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    {% for photo in photo_list %}
        <img src="{{ photo }}">
        {% empty %}
        <p><strong>검색하려는 이미지가 없습니다!</strong></p>
    {% endfor %}
</body>
</html>
```

![](C:\TurtleLab\SSAFY\online-lectures(과제업로드)\0330\workshop\images\캡처2.PNG)

