from django.db import models
from django.utils import timezone

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    page_title = models.CharField(max_length=100)  # Новое поле для идентификации страницы

    def __str__(self):
        return f'Комментарий от {self.name} на {self.created_at}'
