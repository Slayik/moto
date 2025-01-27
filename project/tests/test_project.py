import pytest
from django.urls import reverse
from moto.models import Motorcycle
from moto.forms import MotorcycleForm

# === Тесты моделей ===
@pytest.mark.django_db
def test_motorcycle_creation():
    bike = Motorcycle.objects.create(
        name="Kawasaki Ninja",
        price=15000,
        available=True
    )
    assert bike.name == "Kawasaki Ninja"
    assert bike.price == 15000
    assert bike.available is True


# === Тесты URL-адресов ===
def test_homepage_url(client):
    url = reverse('homepage')  # Замените 'homepage' на имя маршрута
    response = client.get(url)
    assert response.status_code == 200


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
