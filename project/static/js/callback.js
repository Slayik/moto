document.addEventListener('DOMContentLoaded', () => {
    const callbackForm = document.getElementById('callbackForm');

    if (callbackForm) {
        callbackForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Отменяем стандартное поведение формы

            // Получаем CSRF токен
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            // Собираем данные формы
            const formData = new FormData(this);

            // Отправка данных с помощью fetch
            fetch(callbackForm.action, {
                method: "POST",
                body: formData,
                headers: {
                    "X-CSRFToken": csrfToken,
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert(data.message);
                    // Закрытие модального окна после успешной отправки
                    const modal = document.getElementById('callbackModal');
                    const bootstrapModal = bootstrap.Modal.getInstance(modal);
                    bootstrapModal.hide();
                } else {
                    alert(data.message);
                }
            })
            .catch(error => console.error("Ошибка:", error));
        });
    }
});
