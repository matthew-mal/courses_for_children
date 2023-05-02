from django.db import models


class Variant(models.Model):
    title = models.CharField('Название', max_length=20)
    intro = models.CharField('Описание', max_length=150)
    hours = models.IntegerField('Всего заданий')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
