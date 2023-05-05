from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import TaskForm, CourseForm
from .models import Course, Task


def main_courses(request):
    courses = Course.objects.order_by('title')
    return render(request, 'main_courses.html', {'courses': courses})


def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    tasks = course.task_set.all()
    return render(request, 'course_detail.html', {'course': course, 'tasks': tasks})


def task_list(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    tasks = Task.objects.filter(course=course)
    return render(request, 'tasks.html', {'tasks': tasks, 'course': course})


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return self.model.objects.get(pk=pk)


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('courses')


@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_task(request, course_id):
    course = Course.objects.get(id=course_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.course = course
            task.save()
            return redirect('course_detail', course_id=course_id)
    else:
        form = TaskForm()

    context = {'form': form, 'course': course}
    return render(request, 'add_task.html', context)


@user_passes_test(lambda u: u.is_superuser)
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('task_detail', pk=pk)
    return render(request, 'task_update.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def add_course(request):
    error = ''
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('courses')

        else:
            error = 'Форма заполнена неверно'

    form = CourseForm()

    context = {
        'form': form,
        'error': error
    }

    return render(request, 'add_course.html', context)
