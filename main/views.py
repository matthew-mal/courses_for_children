from django.shortcuts import render, redirect
from .models import Reviews
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def feedback(request):
    reviews = Reviews.objects.order_by('date')
    return render(request, 'feedback.html', {'reviews': reviews})


def news_home(request):
    return render(request, 'news.html')


@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.login = request.user  # Установка текущего пользователя в поле "login"
            comment.save()
            return redirect('feedback')
    else:
        form = ReviewForm(initial={'login': request.user})  # Установка начального значения "login" в форме
    return render(request, 'add_review.html', {'form': form})
