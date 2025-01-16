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
    return HttpResponse('About page')

