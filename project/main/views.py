import random
from django.shortcuts import render
from products.models import MotoInStock, MotoToOrder

# Главная страница
def index(request):
    # Получаем все товары из моделей
    moto_to_order = list(MotoToOrder.objects.all())
    moto_in_stock = list(MotoInStock.objects.all())

    # Смешиваем товары и берем 4 случайных
    random_motos = random.sample(moto_to_order + moto_in_stock, 4)

    return render(request, 'main/index.html', {'random_motos': random_motos})

# Страница О нас
def about(request):
    return render(request, 'main/about.html')

# Страница с отзывами
def comments(request):
    return render(request, 'main/comments.html')

# Страница "Мотоциклы в наличии"
def in_stock(request):
    return render(request, 'main/in_stock.html')

# Страница "Мотоциклы под заказ"
def to_order(request):
    return render(request, 'main/to_order.html')

# Страница с экипировкой
def equip(request):
    return render(request, 'main/equip.html')

# Страница с контактами
def contacts(request):
    return render(request, 'main/contacts.html')
