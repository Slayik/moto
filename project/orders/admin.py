from django.contrib import admin
from.models import Order
from.models import Cart
from.models import CartItem
# Register your models here.

admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(CartItem)