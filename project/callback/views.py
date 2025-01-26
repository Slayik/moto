from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from .models import CallbackRequest
import logging

# Создаем логгер для отслеживания ошибок
logger = logging.getLogger(__name__)

@csrf_protect
def callback_request_view(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            phone_number = request.POST.get('phone_number')
            message = request.POST.get('message', '')

            # Проверка, что поля обязательные заполнены
            if not name or not phone_number:
                return JsonResponse({'success': False, 'message': 'Не все обязательные поля заполнены'})

            # Логируем полученные данные для отладки
            logger.debug(f"Received form data: name={name}, phone_number={phone_number}, message={message}")

            # Сохраняем данные в модель
            CallbackRequest.objects.create(
                name=name,
                phone_number=phone_number,
                message=message
            )

            return JsonResponse({'success': True, 'message': 'Ваш запрос успешно отправлен!'})

        except Exception as e:
            logger.error(f"Ошибка при отправке формы: {str(e)}")
            return JsonResponse({'success': False, 'message': f'Ошибка отправки формы: {str(e)}'})

    return JsonResponse({'success': False, 'message': 'Ошибка отправки формы.'})
