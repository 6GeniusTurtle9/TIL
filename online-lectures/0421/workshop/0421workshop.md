# 4월 21일 workshop

### 1. models.py

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
```



### 2. forms.py

```python
from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
```



### 3. views.py

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

***(생략)***

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)

def comments_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
    return redirect('articles:detail', article.pk)

def comments_delete(request, article_pk, comment_pk):
    if request.method == "POST":
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
    return redirect('articles:detail', article_pk)
```

### 4. urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),

    # articles/1/comments/
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'),
    # articles/1/comments/1/delete/
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]
```



### 5. detail.html

```html
{% extends 'base.html' %}

{% block content %}
	<h2>DETAIL</h2>
	<hr>
	<h3>{{ article.pk }}번글</h3>
	<p>제목: {{ article.title }}</p>
	<p>내용: {{ article.content }}</p>
	<p>생성 시각: {{ article.created_at }}</p>
	<p>수정 시각: {{ article.updated_at }}</p>
	<a href="{% url 'articles:index' %}">BACK</a>
	<hr>
	<form action="{% url 'articles:comments_create' article.pk %}" method="POST">
		{% csrf_token %}
		{{ comment_form.as_p }}
		<button>댓글 작성</button>
	</form>
	<hr>
	<h4>댓글 목록({{ article.comment_set.all|length }}개의 댓글이 있습니다.)</h4>
	{% for comment in article.comment_set.all %}
		<p>[{{ comment.pk }}] {{ comment.content }}</p>
		<form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
			{% csrf_token %}
			<input type='submit' value='삭제하기'>
		</form>
	{% empty %}
		<p>댓글이 없습니다</p>
	{% endfor %}
{% endblock %}
```
