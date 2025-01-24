<form id="callbackForm" method="POST">
    {% csrf_token %}
    <input type="text" id="name" name="name" required>
    <input type="text" id="phone" name="phone_number" required>
    <input type="email" id="email" name="email">
    <textarea id="message" name="message"></textarea>
    <button type="submit">Отправить</button>
</form>
