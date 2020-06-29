def kvadr(max):
    a = 1
    b = 1
    while a < max:
        yield b
        if a == 1:
            a += 1
        b = a ** 2
        a += 1
    return []

print('Введите максимальное значение квадрата')
m = int(input())
l = []
for n in kvadr(m):
    if int(n / 10) == 0:
        l.append(n)
    elif int(n / 100) == 0:
        l.append(int(n / 10))
        l.append(int(n % 10))

#print (l)
print('Введите номер цифры')
n = int(input()) - 1
print(l[n])
