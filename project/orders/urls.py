from django.urls import path
from .views import add_to_cart, cart_detail, checkout, order_success
from . import views  # Этот импорт нужен для использования views

# URL patterns для приложения orders

urlpatterns = [
    path('cart/', cart_detail, name='cart_detail'),
    path('orders/cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', checkout, name='checkout'),
    path('success/', order_success, name='order_success'),
]
