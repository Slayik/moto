from django.urls import path
from .views import add_to_cart, cart_detail, checkout, order_success

# URL patterns для приложения orders
urlpatterns = [
    # Отображение корзины пользователя
    path('cart/', cart_detail, name='cart_detail'),

    # Добавление товара в корзину
    # <int:product_id> - ID товара
    # <str:model_name> - имя модели товара (MotoInStock, MotoToOrder или Equipments)
    path('cart/add/<int:product_id>/<str:model_name>/', add_to_cart, name='add_to_cart'),

    # Страница оформления заказа
    path('checkout/', checkout, name='checkout'),

    # Страница успешного оформления заказа
    path('success/', order_success, name='order_success'),
]
