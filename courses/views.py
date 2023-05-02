from django.shortcuts import render
from .models import Variant


def main_courses(request):
    courses = Variant.objects.order_by('title')
    return render(request, 'main_courses.html', {'courses': courses})
