from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    intro = models.CharField('Описание', max_length=150)
    full_news = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
