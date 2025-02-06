from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.contenttypes.models import ContentType
from .models import Cart, CartItem, Order

# Представление для добавления товара в корзину
def add_to_cart(request, product_id, model_name):
    try:
        # Определяем тип товара по имени модели
        content_type = ContentType.objects.get(model=model_name)
        product_model = content_type.model_class()
        product = product_model.objects.get(id=product_id)
    except (ContentType.DoesNotExist, product_model.DoesNotExist):
        return redirect('error_page')  # Перенаправление на страницу ошибки (если нужно)

    # Получаем или создаём корзину
    cart, created = Cart.objects.get_or_create(id=request.session.get('cart_id'))
    request.session['cart_id'] = cart.id

    # Добавляем или обновляем товар в корзине
    cart_item, created = CartItem.objects.get_or_create(
        content_type=content_type,
        object_id=product.id,
        cart=cart
    )
    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart_detail')

# Представление для отображения корзины
def cart_detail(request):
    cart = Cart.objects.filter(id=request.session.get('cart_id')).first()
    return render(request, 'orders/cart_detail.html', {'cart': cart})

# Представление для оформления заказа
def checkout(request):
    cart = Cart.objects.filter(id=request.session.get('cart_id')).first()
    if not cart or not cart.items.exists():
        return redirect('cart_detail')  # Перенаправление на корзину, если она пуста

    if request.method == 'POST':
        # Создаём заказ
        order = Order.objects.create(
            customer_name=request.POST.get('name'),
            customer_email=request.POST.get('email'),
            address=request.POST.get('address')
        )
        order.items.set(cart.items.all())
        order.save()

        # Очищаем корзину и удаляем её ID из сессии
        cart.items.clear()
        request.session.pop('cart_id', None)

        return redirect('order_success')

    return render(request, 'orders/checkout.html', {'cart': cart})

# Представление для успешного заказа
def order_success(request):
    return render(request, 'orders/order_success.html')
