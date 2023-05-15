from django import forms
from .models import Task, Course
from django.forms import ModelForm, TextInput, Textarea, FileInput, NumberInput


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'intro', 'hours')

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название курса'
            }),
            "intro": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое описание'
            }),
            "hours": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество уроков'
            }),
        }


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'hours', 'attached_file', 'course']
