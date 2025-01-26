from django.db import models

class CallbackRequest(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CallbackRequest from {self.name} at {self.created_at}"
