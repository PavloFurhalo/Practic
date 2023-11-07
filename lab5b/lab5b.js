function calculateTriangleArea() {
    const side1 = parseFloat(document.getElementById('side1').value);
    const side2 = parseFloat(document.getElementById('side2').value);
    const side3 = parseFloat(document.getElementById('side3').value);

    const s = (side1 + side2 + side3) / 2;
    const area = Math.sqrt(s * (s - side1) * (s - side2) * (s - side3));

    document.getElementById('result1').innerHTML = `Area: ${area}`;
}

function calculateTriangleAreaWithAngle() {
    const side1 = parseFloat(document.getElementById('side1_2').value);
    const side2 = parseFloat(document.getElementById('side2_2').value);
    const angle = parseFloat(document.getElementById('angle').value);

    const radians = (angle * Math.PI) / 180;
    const area = (side1 * side2 * Math.sin(radians)) / 2;

    document.getElementById('result2').innerHTML = `Area: ${area}`;
}


function calculateTriangleAreaWithHeight() {
    const side = parseFloat(document.getElementById('side3_1').value);
    const height = parseFloat(document.getElementById('height').value);

    const area = (side * height) / 2;

    document.getElementById('result3').innerHTML = `Area: ${area}`;
}

function calculateTriangleAreaWithHeightAlt() {
    const side = parseFloat(document.getElementById('side3_2').value);
    const height = parseFloat(document.getElementById('height2').value);

    const area = (side * height) / 2;

    document.getElementById('result4').innerHTML = `Area: ${area}`;
}

function calculateTriangleAreaWithRadius() {
    const side1 = parseFloat(document.getElementById('side1_5').value);
    const side2 = parseFloat(document.getElementById('side2_5').value);
    const side3 = parseFloat(document.getElementById('side3_5').value);
    const radius = parseFloat(document.getElementById('radius').value);

    const s = (side1 + side2 + side3) / 2;
    const area = (side1 * side2 * side3) / (4 * radius);

    document.getElementById('result5').innerHTML = `Area: ${area}`;
}

function checkPalindrome() {
    const number = parseInt(document.getElementById('palindrome').value);
    const originalNumber = number;
    let reverse = 0;

    while (number > 0) {
        const remainder = number % 10;
        reverse = reverse * 10 + remainder;
        number = Math.floor(number / 10);
    }

    const isPalindrome = originalNumber === reverse;

    document.getElementById('result6').innerHTML = `Is Palindrome: ${isPalindrome}`;
}

function checkAnagram() {
    const word1 = document.getElementById('word1').value.toLowerCase();
    const word2 = document.getElementById('word2').value.toLowerCase();

    const sortedWord1 = word1.split('').sort().join('');
    const sortedWord2 = word2.split('').sort().join('');

    const isAnagram = sortedWord1 === sortedWord2;

    document.getElementById('result7').innerHTML = `Is Anagram: ${isAnagram}`;
}

function getFibonacciNumber() {
    const index = parseInt(document.getElementById('fibIndex').value);

    let fib1 = 0, fib2 = 1, fib = 1;

    for (let i = 2; i <= index; i++) {
        fib = fib1 + fib2;
        fib1 = fib2;
        fib2 = fib;
    }

    document.getElementById('result8').innerHTML = `Fibonacci Number: ${fib}`;
}

function checkFibonacciNumber() {
    const number = parseInt(document.getElementById('fibNumber').value);

    let fib1 = 0, fib2 = 1, fib = 1;

    while (fib < number) {
        fib = fib1 + fib2;
        fib1 = fib2;
        fib2 = fib;
    }

    const isFibonacci = fib === number;

    document.getElementById('result9').innerHTML = `Is Fibonacci Number: ${isFibonacci}`;
}

