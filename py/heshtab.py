hashTable = [[] for _ in range(10)] # Створюється хеш-таблиця з 10 слотами

def checkPrime(n): #Ця функція перевіряє чи є число n простим. Вона повертає 1, якщо число є простим, і 0, якщо ні.
    if n == 1 or n == 0:
        return 0

    for i in range(2, n//2):
        if n % i == 0:
            return 0
    return 1

def getPrime(n): #Ця функція повертає найменше просте число, яке більше або дорівнює n
    if n % 2 == 0:
        n = n + 1
    while not checkPrime(n):
        n += 2
    return n

def hashFunction(key): #Ця фкнкція використовує залишок від ділення ключа на кількість слотів у хеш-таблиці щоб визначити індекс для зберігання пари ключ-значення
    capacity = getPrime(10)
    return key % capacity

def insertData(key, data): #Функція вставки приймає ключ key та відповідне йому значення data. Вона використовує хеш-функцію для визначення індексу в хеш-таблиці та додає пару ключ-значення до відповідного слоту. Якщо у цьому слоті вже є елементи то новий елемент додається до списку
    index = hashFunction(key)
    hashTable[index].append((key, data))

def removeData(key): #Функція видалення приймає ключ key. Вона використовує хеш-функцію щоб знайти слот де міститься цей ключ,потім вона переглядає всі пари ключ-значення у цьому слоті та видаляє ту, де ключ збігається з вхідним ключем
    index = hashFunction(key)
    for item in hashTable[index]:
        if item[0] == key:
            hashTable[index].remove(item)
            break

# Приклад використання
insertData(123, "apple")
insertData(432, "mango")
insertData(213, "banana")
insertData(654, "guava")

print(hashTable)

# Вставка елемента з колізією
insertData(743, "orange")

print(hashTable)

# Видалення елемента
removeData(123)

print(hashTable)
