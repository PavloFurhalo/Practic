queue = []

queue.append(1)
print("1 ввійшов в чергу")
print(queue)
queue.append(2)
print("2 ввійшов в чергу")
print(queue)
queue.append(3)
print("3 ввійшов в чергу")
print(queue)


queue.pop(0)
print("1 вийшов з черги")

print(queue)

queue.pop(0)
print("2 вийшов з черги")

print(queue)



if queue.__len__ == 0:
    print("Черга пуста")

else:
    print("В черзі хтось є")