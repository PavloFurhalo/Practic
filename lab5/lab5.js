document.getElementById('go').addEventListener('click', function() {
    const sourceText = document.getElementById('source-text').value;
    const resultContainer = document.getElementById('result-text');

    resultContainer.innerHTML = '';

    for (let i = 0; i < sourceText.length; i++) {
        const char = sourceText[i];

        if (/^[a-zA-Z]$/.test(char)) {
            const letter = char.toLowerCase();
            const isUpperCase = char === char.toUpperCase();
            const imageName = isUpperCase ? `${letter}.png` : `small_${letter}.png`;

            const image = document.createElement('img');
            image.src = `images/${imageName}`;
            image.alt = char;
            image.style.opacity = '0';
            resultContainer.appendChild(image);

            const delay = 500;

            setTimeout(function() {
                image.style.opacity = '1';
            }, i * delay);
        } else {
            const textNode = document.createTextNode(char);
            resultContainer.appendChild(textNode);
        }
    }
});
