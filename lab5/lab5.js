document.getElementById('go').addEventListener('click', function() {
    const sourceText = document.getElementById('source-text').value;
    const resultContainer = document.getElementById('result-text');

    resultContainer.innerHTML = '';

    for (let i = 0; i < sourceText.length; i++) {
        const letter = sourceText[i].toLowerCase();
        const isUpperCase = sourceText[i] === sourceText[i].toUpperCase();
        const imageName = isUpperCase ? `${letter}.png` : `small_${letter}.png`;
        const image = document.createElement('img');
        image.src = `images/${imageName}`;
        image.alt = letter;
        resultContainer.appendChild(image);
    }
});
