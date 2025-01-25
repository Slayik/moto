<form id="callbackForm" method="POST">
    {% csrf_token %}
    <label for="name">Ваше имя</label>
    <input type="text" id="name" name="name" placeholder="Введите ваше имя" required>
    
    <label for="phone">Ваш номер телефона</label>
    <input type="text" id="phone" name="phone_number" placeholder="Введите ваш номер телефона" required>
    
    <label for="email">Ваш email</label>
    <input type="email" id="email" name="email" placeholder="example@mail.com">
    
    <label for="message">Ваше сообщение</label>
    <textarea id="message" name="message" placeholder="Введите ваше сообщение"></textarea>
    
    <button type="submit">Отправить</button>
</form>
