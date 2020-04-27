# 4월 27일 workshop

> 오늘자 workshop은...끝내지 못했습니다.

### 1. views.py

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vote, Comment
from .forms import VoteForm, CommentForm


# Create your views here.
def index(request):
    votes = Vote.objects.all()
    context = {
        'votes': votes,
    }
    return render(request, 'votes/index.html', context)

def create(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.save()
            vote.user = request.user
            vote.save()
            return redirect('vote:index')
    else:
        form = VoteForm()
    context = { 'form': form }
    return render(request, 'votes/form.html', context)

def detail(request, vote_pk):
    vote = get_object_or_404(Vote, pk=vote_pk)
    context = {
        'vote': vote
    }
    return render(request, 'votes/detail.html', context)

```



### 2. models.py

```python
from django.db import models
from django.conf import settings

# Create your models here.
class Vote(models.Model):
    title = models.CharField(max_length=100)
    score1 = models.IntegerField()
    score2 = models.IntegerField()
    issue1 = models.TextField()
    issue2 = models.TextField()
    issue_choices = (
        (issue1, 'issue1'),
        (issue2, 'issue2'),
        )
    issue = models.CharField(
        max_length=100,
        choices=issue_choices,
        default=issue1,
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
```


