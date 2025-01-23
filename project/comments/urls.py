from django.urls import path
from . import views

urlpatterns = [
    path('page/<str:page_title>/', views.page_detail, name='page_detail'),
    
]
