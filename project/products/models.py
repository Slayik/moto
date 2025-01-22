
from django.db import models

class MotoInStock(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена в $
    image = models.ImageField(upload_to='motos/in_stock/', null=True, blank=True)  # Загрузка изображений
    
    def __str__(self):
        return self.name


class MotoToOrder(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена в $
    image = models.ImageField(upload_to='motos/to_order/', null=True, blank=True)  # Загрузка изображений
    
    def __str__(self):
        return self.name


class Equipments(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена в $
    image = models.ImageField(upload_to='equipments/', null=True, blank=True)  # Загрузка изображений
    
    def __str__(self):
        return self.name
