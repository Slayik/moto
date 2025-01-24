from django.shortcuts import render, redirect
from django.urls import reverse
from .models import CallbackRequest
from django.contrib import messages  # для уведомлений пользователю

def callback_request_view(request):
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Сохраняем данные в модель
        CallbackRequest.objects.create(
            name=name,
            phone_number=phone_number,
            email=email,
            message=message
        )
        # Уведомление об успешной отправке
        messages.success(request, 'Ваш запрос успешно отправлен! Мы свяжемся с вами в ближайшее время.')
        return redirect(reverse('callback_form'))  # возвращаемся на страницу формы

    return render(request, 'callback_form.html')  # шаблон для формы
