a =[]
c = []
couples = []
odd =  []

while True:
    b = input("Enter num: ")
    if b.strip() == "w" :
        break
    
    try:
        b = int(b)
    except ValueError:
        print("It must be int or float")
        continue

    if b >= 0:
        a.append(b)
    elif b < 0:
        c.append(b)

    if b % 2 == 0:
        couples.append(b)
    elif b % 2 != 0:
        odd.append(b)

print(a)
print(c)
print("Парні: ", couples)
print("Непарні: " , odd)