# products/urls.py
from django.urls import path
from . import views

# Определение маршрутов для приложения products
urlpatterns = [
    # Маршрут для страницы мотоциклов в наличии
    # Связан с представлением moto_in_stock_view и доступен по URL '/in_stock/'
    path('in_stock/', views.moto_in_stock_view, name='in_stock'),

    # Маршрут для страницы мотоциклов, доступных под заказ
    # Связан с представлением moto_to_order_view и доступен по URL '/to_order/'
    path('to_order/', views.moto_to_order_view, name='to_order'),

    # Маршрут для страницы списка экипировки
    # Связан с представлением equipments_view и доступен по URL '/equip/'
    path('equip/', views.equipments_view, name='equip'),
]
