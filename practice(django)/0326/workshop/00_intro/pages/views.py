from django.shortcuts import render
import random
# Create your views here.
def lotto(request):
    result=random.sample(range(1,46), 6)
    context = {
        'result':result
    }
    return render(request, 'lotto.html', context)

def dinner(request, menu, people):
    context = {
        'menu': menu,
        'people': people
    }
    return render(request, 'dinner.html', context)


def posts(request, id):
    content = 'Life'
    replies = ['1111', '22222', '유익한들이네용']
    no_replies = []
    user = 'admin'
    context = {
        'id': id,
        'content':content,
        'replies':replies,
        'no_replies':no_replies,
        'user': user,

    }
    return render(request, 'posts.html', context)
