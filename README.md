# Courses for Children

Courses for Children - это веб-приложение, предназначенное для детей,
которое предоставляет доступ к различным курсам, заданиям, статьям и возможность оставлять отзывы.
Приложение разработано с использованием фреймворка Django и использует базу данных PostgreSQL.

Функциональность приложения:
Регистрация и аутентификация пользователей.
Просмотр доступных курсов и заданий.
Чтение статей и полезных материалов.
Оставление отзывов к приложению.

## Установка и настройка

1. Убедитесь, что у вас установлен Python версии 3.x и pip.
2. Склонируйте репозиторий с приложением:
3. Перейдите в директорию проекта:
4. Установите зависимости, указанные в файле `requirements.txt`:
5. Создайте и настройте базу данных PostgreSQL. Убедитесь, что у вас установлен PostgreSQL и доступ к созданию базы данных.

6. В файле `settings.py` приложения, укажите параметры подключения к базе данных PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'your_host',
        'PORT': 'your_port',
    }
}

Приложение еще в процессе





