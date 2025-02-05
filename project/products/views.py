from django.shortcuts import render
from .models import MotoInStock, MotoToOrder, Equipments

# Представление для отображения мотоциклов в наличии
# Получает все объекты модели MotoInStock и передаёт их в шаблон 'in_stock.html'
def moto_in_stock_view(request):
    moto_in_stock = MotoInStock.objects.all()  # Получение всех мотоциклов в наличии
    return render(request, 'main/in_stock.html', {'moto_in_stock': moto_in_stock})  # Рендеринг шаблона с контекстом

# Представление для отображения мотоциклов, доступных под заказ
# Получает все объекты модели MotoToOrder и передаёт их в шаблон 'to_order.html'
def moto_to_order_view(request):
    moto_to_order = MotoToOrder.objects.all()  # Получение всех мотоциклов под заказ
    return render(request, 'main/to_order.html', {'moto_to_order': moto_to_order})  # Рендеринг шаблона с контекстом

# Представление для отображения списка экипировки
# Получает все объекты модели Equipments и передаёт их в шаблон 'equip.html'
def equipments_view(request):
    equipments = Equipments.objects.all()  # Получение всей доступной экипировки
    return render(request, 'main/equip.html', {'equipments': equipments})  # Рендеринг шаблона с контекстом
