from django.contrib import admin
from django.urls import include, path
from main import views as main_views  # Импортируем views из приложения main
from prices import views as prices_views  # Импортируем views из приложения prices

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index, name='index'),  # Главная страница
    path('about/', main_views.about, name='about'),  # Страница "О нас"
    path('comments/', main_views.comments, name='comments'),  # Страница "Отзывы"
    path('in_stock/', main_views.in_stock, name='in_stock'),  # Страница "В наличии"
    path('to_order/', main_views.to_order, name='to_order'),  # Страница "Под заказ"
    path('equip/', main_views.equip, name='equip'),  # Страница "Экипировка"
    path('contacts/', main_views.contacts, name='contacts'),  # Страница "Контакты"
    path('products/', prices_views.product_list, name='product_list'),  # URL для списка товаров
    path('', include('prices.urls')),  # Включаем маршруты приложения prices
    path('prices/', include('prices.urls')),  # Убедитесь, что путь соответствует структуре
]
