a =[]
c = []

while True:
    b = input("Enter num: ")
    if b.strip() == "w" :
        break

    try:
        num = int(b)
    except ValueError:
        print("It must be int or float")
        continue

    if num >= 0:
        a.append(num)
    elif num < 0:
        c.append(num)

print(a)
print(c)