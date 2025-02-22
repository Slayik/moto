import random
from django.shortcuts import render
from .models import MotoInStock, MotoToOrder, Equipments

# Представление для отображения мотоциклов в наличии
def moto_in_stock_view(request):
    moto_in_stock = MotoInStock.objects.all()
    return render(request, 'main/in_stock.html', {'moto_in_stock': moto_in_stock})

# Представление для отображения мотоциклов под заказ
def moto_to_order_view(request):
    moto_to_order = MotoToOrder.objects.all()
    return render(request, 'main/to_order.html', {'moto_to_order': moto_to_order})

# Представление для отображения списка экипировки
def equipments_view(request):
    equipments = Equipments.objects.all()
    return render(request, 'main/equip.html', {'equipments': equipments})


