from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView


def news_home(request):
    news = Articles.objects.order_by('date')
    return render(request, 'news.html', {'news': news})


class NewsAddress(DetailView):
    model = Articles
    template_name = 'details_view.html'
    context_object_name = 'article'


@user_passes_test(lambda u: u.is_superuser)
def add_article(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'add_article.html', data)
