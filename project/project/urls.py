from django.contrib import admin
from django.urls import include, path
from main import views as main_views  # Импортируем views из приложения main
from products import views as products_views  # Импортируем views из приложения products
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index, name='index'),  # Главная страница
    path('about/', main_views.about, name='about'),  # Страница "О нас"
    path('comments/', main_views.comments, name='comments'),  # Страница "Отзывы"
    path('contacts/', main_views.contacts, name='contacts'),  # Страница "Контакты"

    
    # Cтраницы из приложения products
    path('products/in_stock/', products_views.moto_in_stock_view, name='moto_in_stock'),
    path('products/to_order/', products_views.moto_to_order_view, name='moto_to_order'),
    path('products/equipments/', products_views.equipments_view, name='equipments'),
    
    # Подключаем маршруты из приложения products 
    path('products/', include('products.urls')),
    path('comments/', include('comments.urls')),
    path('callback/', include('callback.urls')),

    #Из приложения Users
    #Настрока views
    #Включаем все маршруты из файла users/urls.py
    path('users/', include('users.urls')),
    #из приложения заказы
    path('orders/', include('orders.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)