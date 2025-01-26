from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from .models import CallbackRequest

@csrf_protect  # Оставляем, если вам нужно защитить только это представление
def callback_request_view(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message', '')

        # Сохраняем данные в модель
        CallbackRequest.objects.create(
            name=name,
            phone_number=phone_number,
            message=message
        )

        return JsonResponse({'success': True, 'message': 'Ваш запрос успешно отправлен!'})

    return JsonResponse({'success': False, 'message': 'Ошибка отправки формы.'})
