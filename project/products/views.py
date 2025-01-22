from django.shortcuts import render
from .models import MotoInStock, MotoToOrder, Equipments

def moto_in_stock_view(request):
    moto_in_stock = MotoInStock.objects.all()
    return render(request, 'main/in_stock.html', {'moto_in_stock': moto_in_stock})

def moto_to_order_view(request):
    moto_to_order = MotoToOrder.objects.all()
    return render(request, 'main/to_order.html', {'moto_to_order': moto_to_order})

def equipments_view(request):
    equipments = Equipments.objects.all()
    return render(request, 'main/equip.html', {'equipments': equipments})
