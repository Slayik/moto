from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#Главная страница
def index(request):
    context: dict[str, str] = {
        'title': 'Home',
        'content': 'Главная страница магазина'
    }
    return render(request, 'main/index.html', context)

#Страница О нас
def about(request):
    return render(request, 'main/about.html')

def comments(request):
    return render(request, 'main/comments.html')

def index(request):
    return render(request, 'main/index.html')

def in_stock(request):
    return render(request, 'main/in_stock.html')

def to_order(request):
    return render(request, 'main/to_order.html')

def equip(request):
    return render(request, 'main/equip.html')

def contacts(request):
    return render(request, 'main/contacts.html')