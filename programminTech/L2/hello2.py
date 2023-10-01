print('Hello', 'world', sep=',', end='.')
# ? a = 0
# ? b = 3
# ? print(a or b)
a = input()
if a.lower() == 'teacher':  # type(a) is str
    print('hello teacher')
    print(len(a))
    if a == 'a':
        print('a')
elif a == 't':
    print('elif')
else:
    print(0)


a = int(input())
if a > 0:
    print('+')
else:
    print('-')


a = 'salam'
for i in range(5, 120, 5):
    print(i)

print(a.center(20))
print(a.index('s'))
print(a.join(a))
print(a.replace('s', 'd'))
