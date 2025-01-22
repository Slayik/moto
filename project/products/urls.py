# products/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('in_stock/', views.moto_in_stock_view, name='in_stock'),
    path('to_order/', views.moto_to_order_view, name='to_order'),
    path('equip/', views.equipments_view, name='equip'),
]
