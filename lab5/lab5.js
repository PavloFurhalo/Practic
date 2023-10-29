function showImages() {
    const inputField = document.getElementById('input-field');
    const imageContainer = document.getElementById('image-container');
    const inputValue = inputField.value.toLowerCase(); // Перетворення на нижній регістр

    // Очищення контейнера перед вставкою нових картинок
    imageContainer.innerHTML = '';

    for (let i = 0; i < inputValue.length; i++) {
        const letter = inputValue[i];
        
        // Перевірка, чи є введене значення літерою
        if (/^[a-zA-Z]$/.test(letter)) {
            const image = document.createElement('img');
            image.src = `${letter}.png`; // Припустимо, що ваші файли мають імена "a.png", "b.png", і так далі
            imageContainer.appendChild(image);
        }
    }
}
