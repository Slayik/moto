from django.urls import path
from .views import register_view, login_view, logout_view, profile_view
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Страница регистрации нового пользователя
    path('register/', register_view, name='register'),  
     
    # Страница выхода пользователя
    path('logout/', logout_view, name='logout'),  
    
    # Страница профиля пользователя
    path('profile/', profile_view, name='profile'),  
    
    # Стандартная страница входа через LoginView, редиректит авторизованных пользователей
    path('login/', LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True), name='login'),

     # Маршруты для сброса пароля
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    
]
