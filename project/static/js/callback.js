document.addEventListener('DOMContentLoaded', () => {
    const e = { module_or_path: "value" }; // Пример корректного объекта

    // Проверяем, является ли переменная e объектом
    if (typeof e !== "undefined" && Object.getPrototypeOf(e) === Object.prototype) {
        console.log("Параметры:", e); // Логируем объект для проверки
    } else {
        console.warn("Используются устаревшие параметры. Передавайте параметры как единый объект.");
    }

    // Пример использования объекта
    const config = {
        module_or_path: e.module_or_path // Присваиваем значение
    };

    console.log("Конфигурация:", config);
});
