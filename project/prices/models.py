# models.py  
from django.db import models  

class Price(models.Model):  
    item_name = models.CharField(max_length=100)   # Название товара или услуги  
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цены  

    def __str__(self):  
        return f"{self.item_name}: {self.price} $."