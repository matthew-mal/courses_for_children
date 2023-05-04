from django.db import models
from django.urls import reverse


class Course(models.Model):
    title = models.CharField('Название', max_length=20)
    intro = models.CharField('Описание', max_length=150)
    hours = models.IntegerField('Всего заданий')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Task(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=20)
    description = models.CharField('Описание', max_length=150)
    hours = models.IntegerField('Всего заданий')
    attached_file = models.FileField(upload_to='tasks/')

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])
