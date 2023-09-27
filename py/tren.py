a = []
c = []
d = []
o = []
while True:
    b = input("Введіть число: ")
    a.append(b)
    if b == "w":
        a.pop()
        break

if a[0] >= 0:
    a.append(b)
    a.pop(0)
elif a[0] < 0:
    c.append(b)
    a.pop[0]

if a[0] % 2 == 0:
    d.append(b)
    a.pop[0]
elif a[0] % 2 != 0:
     o.append(b)
     a.pop[0]


print(a)
print(c)
print(d)
print(o)


