"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path

# Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Базовые настройки ---
# Секретный ключ (не публикуйте его в продакшене)
SECRET_KEY = 'django-insecure-^mlszi+vod#55e&=8fr#)ju&)gcj5zhr@h6dgmpwp#7@mdiq50'

# Режим отладки (DEBUG = True использовать только в разработке)
DEBUG = True

# Список допустимых хостов (в разработке может быть пустым)
ALLOWED_HOSTS = []

# --- Приложения ---
INSTALLED_APPS = [
    'django.contrib.admin',  # Админка
    'django.contrib.auth',  # Аутентификация
    'django.contrib.contenttypes',  # Типы контента
    'django.contrib.sessions',  # Сессии
    'django.contrib.messages',  # Система сообщений
    'django.contrib.staticfiles',  # Статические файлы
    'orders',  # Приложение "Заказы"
    'main',  # Основное приложение
    'products',  # Приложение "Продукты"
    'comments',  # Приложение "Комментарии"
    'callback',  # Приложение "Обратный звонок"
    'users',  # Приложение "Пользователи"
]

# --- Middleware (промежуточный слой обработки запросов) ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Безопасность
    'django.contrib.sessions.middleware.SessionMiddleware',  # Управление сессиями
    'django.middleware.common.CommonMiddleware',  # Обработка стандартных запросов
    'django.middleware.csrf.CsrfViewMiddleware',  # Защита от CSRF-атак
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Аутентификация
    'django.contrib.messages.middleware.MessageMiddleware',  # Сообщения
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Защита от кликджекинга
]

# Главный файл маршрутов (urls.py проекта)
ROOT_URLCONF = 'project.urls'

# --- Шаблоны ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Движок шаблонов
        'DIRS': [],  # Дополнительные пути к шаблонам (можно добавить BASE_DIR / "templates")
        'APP_DIRS': True,  # Включает поиск шаблонов в папках templates каждого приложения
        'OPTIONS': {
            'context_processors': [  # Контекстные процессоры для шаблонов
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI-приложение (точка входа для сервера)
WSGI_APPLICATION = 'project.wsgi.application'

# --- База данных ---
# Используется SQLite (для продакшена обычно используют PostgreSQL, MySQL или другие СУБД)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- Валидация паролей ---
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Запрет на пароли, похожие на имя пользователя
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Минимальная длина пароля
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Запрет на популярные пароли
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Запрет на чисто цифровые пароли
    },
]

# --- Локализация ---
LANGUAGE_CODE = 'en-us'  # Язык
TIME_ZONE = 'UTC'  # Часовой пояс
USE_I18N = True  # Использовать интернационализацию
USE_TZ = True  # Использовать часовые зоны

# --- Статические файлы ---
STATIC_URL = '/static/'  # URL для статических файлов
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Папка для пользовательских статических файлов
]

# --- Медиа-файлы ---
MEDIA_URL = '/media/'  # URL для медиа-файлов
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Директория для медиа-файлов

# --- Cookies ---
CSRF_COOKIE_NAME = 'csrftoken'  # Имя куки для CSRF-токена
CSRF_COOKIE_HTTPONLY = True  # Защита от доступа к куки через JavaScript
CSRF_USE_SESSIONS = False  # Хранение CSRF-токенов в сессиях (по умолчанию False)

# --- Логин и логаут ---
LOGIN_REDIRECT_URL = '/'  # Куда перенаправлять после входа
LOGOUT_REDIRECT_URL = '/'  # Куда перенаправлять после выхода

# --- Email-настройки ---
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # SMTP-сервер Gmail
EMAIL_PORT = 587  # Порт для TLS
EMAIL_USE_TLS = True  # Использовать TLS
EMAIL_HOST_USER = 'your_email@gmail.com'  # Email для отправки писем
EMAIL_HOST_PASSWORD = 'your_email_password'  # Пароль или пароль приложения
DEFAULT_FROM_EMAIL = 'your_email@gmail.com'  # Email отправителя

# --- Настройка по умолчанию для автоинкрементных полей ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
