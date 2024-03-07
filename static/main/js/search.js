document.getElementById('searchIcon').addEventListener('click', function(event) {
    event.preventDefault(); // отменяем стандартное действие браузера при клике на ссылку
    
    var searchTerm = document.getElementById('searchInput').value;
    
    // Здесь можно добавить код для выполнения поиска с использованием введенного в поле searchTerm значения
    console.log('Выполняется поиск для запроса: ', searchTerm);
    // Например, можно вызвать функцию для выполнения поиска
    searchFunction(searchTerm);
});

function searchFunction(searchTerm) {
    // Здесь можно написать логику выполнения поиска, например отправить AJAX-запрос на сервер для получения результатов
    // На текущем этапе я просто выведу сообщение о выполнении поиска
    console.log('Поиск выполнен для запроса: ', searchTerm);
}