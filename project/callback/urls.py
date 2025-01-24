from django.urls import path
# В файле urls.py вашего приложения callback
from . import views

urlpatterns = [
    # другие URL
    path('callback/', views.callback_request_view, name='callback_request_view'),
]
