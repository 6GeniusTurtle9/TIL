# 3월 26일 workshop

<img src="C:\TurtleLab\SSAFY\online-lectures(과제업로드)\0326\workshop\images\lotto.PNG" style="zoom:75%;" />



### 1. intro/urls.py

```python
from django.contrib import admin
from django.urls import path
from pages import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('lotto/', views.lotto),
]
```



### 2. pages/view.py

```python
from django.shortcuts import render
import random
# Create your views here.
def lotto(request):
    result=random.sample(range(1,46), 6)
    context = {
        'result':result
    }
    return render(request, 'lotto.html', context)
```



### 3. templates/lotto.html

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
    <h1>로또번호 추첨</h1>
    <h2>SSAFY님의 로또번호는 {{ result }}입니다.</h2>
</body>
</html>
```

