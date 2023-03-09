function update_Image_canny() {
    var image = document.getElementById('image_canny');
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            image.src = URL.createObjectURL(xhr.response);
        }
    };
    xhr.open('GET', '/image_canny', true);
    xhr.responseType = 'blob';
    xhr.send();
}
function update_Image_laplass() {
    var image = document.getElementById('image_laplass');
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            image.src = URL.createObjectURL(xhr.response);
        }
    };
    xhr.open('GET', '/image_laplass', true);
    xhr.responseType = 'blob';
    xhr.send();
}
function update_Image_sharra() {
    var image = document.getElementById('image_sharra');
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            image.src = URL.createObjectURL(xhr.response);
        }
    };
    xhr.open('GET', '/image_sharra', true);
    xhr.responseType = 'blob';
    xhr.send();
}
function update_Image_sobel() {
    var image = document.getElementById('image_sobel');
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            image.src = URL.createObjectURL(xhr.response);
        }
    };
    xhr.open('GET', '/image_sobel', true);
    xhr.responseType = 'blob';
    xhr.send();
}
setInterval(update_Image_canny, 1000); // Обновляем изображение каждую секунду
setInterval(update_Image_laplass, 1000); // Обновляем изображение каждую секунду
setInterval(update_Image_sharra, 1000); // Обновляем изображение каждую секунду
setInterval(update_Image_sobel, 1000); // Обновляем изображение каждую секунду