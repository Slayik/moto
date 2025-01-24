from django.contrib import admin
from .models import CallbackRequest

# Register your models here.

class CallbackRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'created_at')  # что показываем в списке
    list_filter = ('created_at',)  # фильтры для удобства поиска
    search_fields = ('name', 'phone_number', 'email')  # по каким полям можно искать
    ordering = ('-created_at',)  # сортировка по дате (от самых новых)


admin.site.register(CallbackRequest, CallbackRequestAdmin)

