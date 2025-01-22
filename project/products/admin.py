

# Register your models here.
from django.contrib import admin
from .models import MotoInStock, MotoToOrder, Equipments

# Регистрируем модели в админке
admin.site.register(MotoInStock)
admin.site.register(MotoToOrder)
admin.site.register(Equipments)