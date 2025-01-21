from django.shortcuts import render

# Главная страница
def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница магазина'
    }
    return render(request, 'main/index.html', context)

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
