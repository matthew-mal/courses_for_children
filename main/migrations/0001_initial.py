# Generated by Django 4.2 on 2023-04-25 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20, verbose_name='Логин')),
                ('feedback', models.CharField(max_length=150, verbose_name='Отзыв')),
                ('points', models.IntegerField(max_length=10, verbose_name='Рейтинг')),
                ('date', models.DateTimeField(verbose_name='Время отзыва')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
