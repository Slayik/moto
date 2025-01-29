import pytest
from django.urls import reverse
from django.utils import timezone
from callback.models import CallbackRequest 
from comments.models import Comment
from products.models import MotoInStock, MotoToOrder, Equipments



#Тесты моделей
# === Тесты модели CallbackRequest ===
@pytest.mark.django_db
def test_callback_request_creation():
    callback = CallbackRequest.objects.create(
        name="John Doe",
        phone_number="1234567890",
        message="I am interested in a motorcycle",
    )
    assert callback.name == "John Doe"
    assert callback.phone_number == "1234567890"
    assert callback.message == "I am interested in a motorcycle"
    assert callback.created_at is not None

# === Тесты модели Comment ===
@pytest.mark.django_db
def test_comment_creation():
    comment = Comment.objects.create(
        name="Jane Doe",
        email="jane.doe@example.com",
        text="Great service!",
        created_at=timezone.now()
    )
    assert comment.name == "Jane Doe"
    assert comment.email == "jane.doe@example.com"
    assert comment.text == "Great service!"
    assert comment.created_at is not None

# === Тесты модели MotoInStock ===
@pytest.mark.django_db
def test_moto_in_stock_creation():
    moto = MotoInStock.objects.create(
        name="Yamaha R1",
        description="Sport motorcycle",
        price=15000.00,
    )
    assert moto.name == "Yamaha R1"
    assert moto.description == "Sport motorcycle"
    assert moto.price == 15000.00

# === Тесты модели MotoToOrder ===
@pytest.mark.django_db
def test_moto_to_order_creation():
    moto_order = MotoToOrder.objects.create(
        name="Harley Davidson",
        description="Cruiser motorcycle",
        price=20000.00,
    )
    assert moto_order.name == "Harley Davidson"
    assert moto_order.description == "Cruiser motorcycle"
    assert moto_order.price == 20000.00

# === Тесты модели Equipments ===
@pytest.mark.django_db
def test_equipment_creation():
    equipment = Equipments.objects.create(
        name="Helmet",
        description="Safety gear",
        price=200.00,
    )
    assert equipment.name == "Helmet"
    assert equipment.description == "Safety gear"
    assert equipment.price == 200.00


# === Тесты URL-адресов ===

#Тесты доступности URL
@pytest.mark.django_db
def test_callback_request_url(client):
    response = client.get(reverse('index'))  # имя вашего URL
    assert response.status_code == 200

@pytest.mark.django_db
def test_callback_request_url(client):
    response = client.get(reverse('in_stock'))  
    assert response.status_code == 200

@pytest.mark.django_db
def test_callback_request_url(client):
    response = client.get(reverse('to_order')) 
    assert response.status_code == 200

@pytest.mark.django_db
def test_callback_request_url(client):
    response = client.get(reverse('equip'))  
    assert response.status_code == 200

@pytest.mark.django_db
def test_callback_request_url(client):
    response = client.get(reverse('about')) 
    assert response.status_code == 200

@pytest.mark.django_db
def test_callback_request_url(client):
    response = client.get(reverse('contacts'))  
    assert response.status_code == 200

@pytest.mark.django_db
def test_callback_request_url(client):
    response = client.get(reverse('comments'))  
    assert response.status_code == 200


#Тест неправильного URL
@pytest.mark.django_db
def test_invalid_url(client):
    response = client.get('/invalid-url/')  #несуществующий URL
    assert response.status_code == 404




# === Тесты представлений ===
@pytest.mark.django_db
def test_motorcycle_list_view(client):
    url = reverse('motorcycle_list')  # Замените на имя маршрута
    response = client.get(url)
    assert response.status_code == 200
    assert 'motorcycle_list.html' in [t.name for t in response.templates]


# === Тесты форм ===
def test_valid_motorcycle_form():
    form = MotorcycleForm(data={
        'name': 'Yamaha R1',
        'price': 20000,
        'available': True
    })
    assert form.is_valid()

def test_invalid_motorcycle_form():
    form = MotorcycleForm(data={
        'name': '',  # Пустое имя
        'price': -5000,  # Недопустимая цена
        'available': True
    })
    assert not form.is_valid()
    assert 'name' in form.errors
    assert 'price' in form.errors


# === Тесты API (если используется DRF) ===
@pytest.mark.django_db
def test_get_motorcycles_api(client):
    response = client.get('/api/motorcycles/')  # Замените на реальный URL
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# === Тесты шаблонов ===
def test_homepage_template_content(client):
    url = reverse('homepage')  # Замените на имя маршрута
    response = client.get(url)
    assert response.status_code == 200
    assert b'Добро пожаловать!' in response.content  # Замените на реальный текст


# === Тесты авторизации ===
@pytest.mark.django_db
def test_protected_view_redirect(client):
    url = reverse('protected_view')  # Замените на защищённый маршрут
    response = client.get(url)
    assert response.status_code == 302  # Редирект на страницу логина
    assert '/login/' in response.url
