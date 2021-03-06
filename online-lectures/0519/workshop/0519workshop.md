# 5월 19일 workshop

### 1. index.html

```html
{% extends 'base.html' %}

{% block content %}
  <h2>INDEX</h2>
  {% for article in articles %}
    <h3>작성자: {{ article.user }}</h3>
    <h4>제목: {{ article.title }}</h4>
    <p>내용: {{ article.content }}</p>
    
      {% if user in article.like_users.all %}
        <i data-id="{{ article.pk }}" class="fas fa-heart fa-lg like-button" style="color:crimson; cursor: pointer;"></i>
      {% else %}
        <i data-id="{{ article.pk }}" class="fas fa-heart fa-lg like-button" style="color:black; cursor: pointer;"></i>
      {% endif %}
    
    <span id="like-count-{{ article.pk }}">{{ article.like_users.all|length }}</span> 명이 이 글을 좋아합니다.
    <hr>
  {% endfor %}
  <a href="{% url 'articles:create' %}">CREATE</a>
    <script>
      // As-Is : 좋아요 클릭 -> a태그  -> like 함수 -> index 함수 -> 전체를 다시 렌더링 (하트 '하나' 때문에)
      // To Be : 좋아요 클릭 -> 이벤트 -> like 함수 -> 일부만 다시 렌더링 (하트 '하나'만)

      // 1. 각 게시글에 포함된 좋아요 버튼 가져오기
      const likeButtons = document.querySelectorAll('.like-button')
      // 2. 각 좋아요 버튼에 이벤트 리스너 등록하기
      likeButtons.forEach(function(likeButton) {
        likeButton.addEventListener('click', function(event) {
          // 3. 각 게시글 버튼을 구분하기 위해 'data-id'(Article PK) 가져오기
          const articleId = event.target.dataset.id
          // 4. Axios를 통해 Like 함수 요청 보내기  (좋아요 여부 & 좋아요 개수)
          axios.get(`/articles/${articleId}/like`)
            .then(response => {
              
              // 5. 좋아요 색깔 변경 (liked true or false)
              if (response.data.liked) {
                  event.target.style.color = 'crimson'
              } else{   // 좋아요 해제 했을 때
              event.target.style.color = 'black'
              }
              // 6. 좋아요 개수
              document.querySelector(`#like-count-${articleId}`).innerText = response.data.like_count
            })
            .catch(error => {
              console.log(error)
            })
        })
      })
    </script>
{% endblock %}


```



### 2. views.py

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Article
from .forms import ArticleForm


def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/form.html', context)


def like(request, article_pk):
    user = request.user 
    article = get_object_or_404(Article, pk=article_pk)
    
    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
        # 좋아요 취소
        liked = False
    else:
        article.like_users.add(user)
        # 좋아요 등록
        liked = True

    return JsonResponse({
            'liked': liked,
            'like_count': article.like_users.count(),
    })
```
