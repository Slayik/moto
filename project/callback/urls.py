from django.urls import path
from . import views

urlpatterns = [
    # другие URL
    path('', views.callback_request_view, name='callback_request_view'),
]
