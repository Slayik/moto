from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from .models import CallbackRequest

@csrf_protect
def callback_request_view(request):
    if request.method == 'POST':
        try:
            # Получаем данные из формы
            name = request.POST.get('name')
            phone_number = request.POST.get('phone_number')
            message = request.POST.get('message', '')

            # Проверка, что обязательные поля заполнены
            if not name or not phone_number:
                return JsonResponse({'success': False, 'message': 'Не все обязательные поля заполнены'})

            # Сохраняем данные в модель
            CallbackRequest.objects.create(
                name=name,
                phone_number=phone_number,
                message=message
            )

            # Возвращаем успешный ответ
            return JsonResponse({'success': True, 'message': 'Ваш запрос успешно отправлен!'})

        except Exception as e:
            # Возвращаем ошибку при исключении
            return JsonResponse({'success': False, 'message': f'Ошибка отправки формы: {str(e)}'})

    # Если метод не POST, возвращаем ошибку
    return JsonResponse({'success': False, 'message': 'Ошибка отправки формы.'})
