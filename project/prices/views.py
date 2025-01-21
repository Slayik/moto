# views.py  
from django.shortcuts import render  
from .models import Price  # Импортируем вашу модель  

def product_list(request):  
    prices = Price.objects.all()  # Получаем все товары из модели Price  
    return render(request, 'main/in_stock.html', {'prices': prices})  # Указываем путь к шаблону и передаем data