from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models

class CartItem(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Связь с моделью товара
    object_id = models.PositiveIntegerField()  # ID объекта
    product = GenericForeignKey('content_type', 'object_id')  # Универсальная связь
    quantity = models.PositiveIntegerField(default=1)  # Количество

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class Cart(models.Model):
    items = models.ManyToManyField(CartItem, blank=True)  # Связь с элементами корзины
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return sum(item.product.price * item.quantity for item in self.items.all())

class Order(models.Model):
    items = models.ManyToManyField(CartItem)  # Привязка к товарам из корзины
    created_at = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    address = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.total_price:
            self.total_price = sum(item.product.price * item.quantity for item in self.items.all())
        super().save(*args, **kwargs)
