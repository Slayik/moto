from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.contrib.auth.models import User


# Модель товара
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


# Модель элемента корзины
class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='items')  # Привязка к корзине
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Связь с моделью товара
    object_id = models.PositiveIntegerField()  # ID объекта
    product = GenericForeignKey('content_type', 'object_id')  # Универсальная связь
    quantity = models.PositiveIntegerField(default=1)  # Количество

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def get_total_price(self):
        return self.product.price * self.quantity


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')  # Привязка к пользователю
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def total_price(self):
        return sum(item.get_total_price() for item in self.items.all())

    def __str__(self):
        return f"Cart {self.id} for {self.user.username}"



# Модель заказа
class Order(models.Model):
    items = models.ManyToManyField(CartItem)  # Связь с товарами из корзины
    created_at = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    address = models.TextField()

    def total_price(self):
        return sum(item.get_total_price() for item in self.items.all())

    def __str__(self):
        return f"Order {self.id} - {self.customer_name}"
