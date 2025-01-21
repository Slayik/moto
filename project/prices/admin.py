# admin.py  
from django.contrib import admin  
from .models import Price  

class PriceAdmin(admin.ModelAdmin):  
    list_display = ('item_name', 'price')  # Поля для отображения в списке  
    search_fields = ('item_name',)  # Поле для поиска  

admin.site.register(Price, PriceAdmin)