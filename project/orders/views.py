from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.contenttypes.models import ContentType
from .models import Cart, CartItem, Order
from products.models import MotoInStock, MotoToOrder, Equipments  # Импортируем нужные модели

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

def add_to_cart(request, product_id, product_type):
    """
    Функция добавления товара в корзину.
    :param product_type: тип товара ('in_stock', 'to_order' или 'equipments')
    """
    # Получаем товар в зависимости от типа
    if product_type == 'in_stock':
        product = get_object_or_404(MotoInStock, id=product_id)
    elif product_type == 'to_order':
        product = get_object_or_404(MotoToOrder, id=product_id)
    elif product_type == 'equipments':
        product = get_object_or_404(Equipments, id=product_id)
    else:
        return redirect('cart_detail')  # Перенаправляем в случае неверного типа

    # Определяем тип модели через ContentType
    content_type = ContentType.objects.get_for_model(product)

    # Проверяем, есть ли активная корзина в сессии
    cart_id = request.session.get('cart_id')
    if cart_id:
        cart = get_object_or_404(Cart, id=cart_id)
    else:
        # Создаем новую корзину, если её нет
        cart = Cart.objects.create(user=request.user)  # Привязываем корзину к пользователю
        request.session['cart_id'] = cart.id

    # Пытаемся найти существующий элемент корзины
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        content_type=content_type,
        object_id=product.id,
    )

    if not created:
        # Если товар уже в корзине — увеличиваем количество
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_detail')  # Перенаправляем на страницу корзины

def remove_from_cart(request, product_id, product_type):
    """
    Функция удаления товара из корзины.
    :param product_type: тип товара ('in_stock', 'to_order' или 'equipments')
    """
    # Получаем товар в зависимости от типа
    if product_type == 'in_stock':
        product = get_object_or_404(MotoInStock, id=product_id)
    elif product_type == 'to_order':
        product = get_object_or_404(MotoToOrder, id=product_id)
    elif product_type == 'equipments':
        product = get_object_or_404(Equipments, id=product_id)
    else:
        return redirect('cart_detail')  # Перенаправляем в случае неверного типа

    # Определяем тип модели через ContentType
    content_type = ContentType.objects.get_for_model(product)

    # Получаем корзину из сессии
    cart = Cart.objects.filter(id=request.session.get('cart_id')).first()
    if cart:
        # Ищем товар в корзине
        cart_item = cart.items.filter(content_type=content_type, object_id=product.id).first()
        if cart_item:
            # Удаляем товар из корзины
            cart_item.delete()

    return redirect('cart_detail')  # Перенаправляем на страницу корзины