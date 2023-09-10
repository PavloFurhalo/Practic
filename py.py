import collections

a = collections.deque()


a.append(1)
print('1 ввійшов')
a.append(2)
print('2 ввійшов')
a.append(3)
print('3 ввійшов')
a.append(4)
print('4 ввійшов')
a.popleft()
print('1 вийшов')
a.popleft()
print('2 вийшов')
a.popleft()
print('3 вийшов')
a.popleft()
print('4 вийшов')

print(a)