from django.shortcuts import render
from .models import Reviews


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def feedback(request):
    reviews = Reviews.objects.order_by('date')
    return render(request, 'feedback.html', {'reviews': reviews})


def news_home(request):
    return render(request, 'news.html')

