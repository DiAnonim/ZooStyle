function getCookie(name) {
    let valueCookie = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                valueCookie = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return valueCookie;
}

function filterProducts(categoryId, filterUrl) { // Добавляем параметр filterUrl
    var productsContainer = document.getElementById("products-container");
    if (!productsContainer) {
        console.error("Products container with id 'products-container' not found");
        return;
    }

    var csrftoken = getCookie("csrftoken");
    console.log("URL запроса:", filterUrl); // Теперь будет реальный URL

    var params = {};
    if (categoryId) {
        params.category_id = categoryId;
        console.log("Категория выбрана:", categoryId);
    }

    fetch(filterUrl + "?" + new URLSearchParams(params), { // Используем переданный URL
        method: 'GET',
        headers: {
            'X-CSRFToken': csrftoken,
            'Accept': 'application/json',
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log("Данные ответа:", data);
        productsContainer.innerHTML = data.products_html;
    })
    .catch(error => {
        console.error("Error when filtering products:", error);
    });
}


document.addEventListener("DOMContentLoaded", () => {
    const categoryLinks = document.querySelectorAll('.category-link');
    categoryLinks.forEach(link => {
        link.addEventListener("click", function(event) {
            event.preventDefault();
            const categoryId = this.getAttribute('data-category-id');
            // Получаем URL из HTML, где он был сгенерирован Django
            const filterUrl = document.getElementById('filter-url-span').getAttribute('data-url'); 
            filterProducts(categoryId, filterUrl); // Передаем URL в функцию
        });
    });
});