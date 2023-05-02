from django.db import models


class Reviews(models.Model):
    login = models.CharField('Логин', max_length=20)
    feedback = models.CharField('Отзыв', max_length=150)
    date = models.DateTimeField('Время отзыва')

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'