"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from main import views
from .views import product_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),  # Страница "О нас"
    path('comments/', views.comments, name='comments'),  # Страница "Отзывы"
    path('in_stock/', views.in_stock, name='in_stock'),  # Страница "В наличии"
    path('to_order/', views.to_order, name='to_order'),  # Страница "Под заказ"
    path('equip/', views.equip, name='equip'),  # Страница "Экипировка"
    path('contacts/', views.contacts, name='contacts'),  # Страница "Контакты"
    path('products/', product_list, name='product_list'),  # URL для списка товаров
    path('', include('prices.urls')),  # Включаем маршруты приложения prices
]
