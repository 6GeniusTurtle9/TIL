from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def review_list(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'community/review_list.html', context)


def new_review(request):
    return render(request, 'community/new_review.html')

def create_review(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    rank = request.GET.get('rank')

    reviews = Review(title=title, content=content, rank=rank)
    reviews.save()

    return redirect('/community')

def review_detail(request, pk):
    review = Review.objects.get(id=pk)
    context = {
        'review':review
    }
    return render(request, 'community/review_detail.html', context)