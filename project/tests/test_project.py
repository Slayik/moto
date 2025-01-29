import pytest
from django.urls import reverse
from django.utils import timezone
from callback.models import CallbackRequest 
from comments.models import Comment
from products.models import MotoInStock, MotoToOrder, Equipments
from comments.forms import CommentForm
from django.contrib.auth.models import User
from django.test import Client, TestCase




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
def test_index_view(client):
    url = reverse('index')  # Главная страница
    response = client.get(url)
    assert response.status_code == 200
    assert 'main/index.html' in [t.name for t in response.templates]  

@pytest.mark.django_db
def test_about_view(client):
    url = reverse('about')  # "О нас"
    response = client.get(url)
    assert response.status_code == 200
    assert 'main/about.html' in [t.name for t in response.templates]  

@pytest.mark.django_db
def test_comments_view(client):
    url = reverse('comments')  # "Отзывы"
    response = client.get(url)
    assert response.status_code == 200
    assert 'main/comments.html' in [t.name for t in response.templates] 

@pytest.mark.django_db
def test_contacts_view(client):
    url = reverse('contacts')  # "Контакты"
    response = client.get(url)
    assert response.status_code == 200
    assert 'main/contacts.html' in [t.name for t in response.templates]  



# === Тесты форм ===
def test_valid_comment_form():
    form = CommentForm(data={
        'name': 'Alex',
        'email': '123qwe@gmail.com',
        'text': 'This is a comment.'
    })
    assert form.is_valid()


    

# === Тесты API (если используется DRF) ===
#@pytest.mark.django_db
#def test_get_motorcycles_api(client):
   # response = client.get('/api/motorcycles/')  # Замените на реальный URL
   # assert response.status_code == 200
   # assert isinstance(response.json(), list)


# === Тесты шаблонов ===
def test_homepage_template_content(client):
    url = reverse('index')  # имя маршрута
    response = client.get(url)
    assert response.status_code == 200
    
    content = response.content.decode('utf-8')  # Декодируем контент
    print(content)  # Для отладки: выводим содержимое ответа
    assert 'МОТОЦИКЛЫ' in content


# === Тесты авторизации ===


class UserAuthTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_view(self):
        # Делаем POST-запрос к представлению входа
        url = reverse('login')  # Используем имя маршрута для входа
        response = self.client.post(url, {'username': 'testuser', 'password': 'testpassword'})

        # Проверяем, что статус ответа 302 (перенаправление после успешного входа)
        self.assertEqual(response.status_code, 302)

        # Проверяем, что пользователь аутентифицирован
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_profile_view_authenticated(self):
        # Аутентификация пользователя
        self.client.login(username='testuser', password='testpassword')

        # Делаем GET-запрос к представлению профиля
        url = reverse('profile')  # Используем имя маршрута для профиля
        response = self.client.get(url)

        # Проверяем, что статус ответа 200 (успех)
        self.assertEqual(response.status_code, 200)

    def test_profile_view_unauthenticated(self):
        # Делаем GET-запрос к представлению профиля без аутентификации
        url = reverse('profile')  # Используем имя маршрута для профиля
        response = self.client.get(url)

        # Проверяем, что статус ответа 302 (перенаправление на страницу входа)
        self.assertEqual(response.status_code, 302)


