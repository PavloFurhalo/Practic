const resultElement = document.getElementById('result')
const input1 = document.getElementById('inp1')
const input2 = document.getElementById('inp2')
const confirm = document.getElementById('confirm')

confirm.onclick = () => {
    console.log(123)
    console.log(resultElement)
    const sum = Number(input1.value) + Number(input2.value)
    resultElement.textContent = `Результат: ${sum}`
}


