def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b
    return []


print('Введите максимальное значение')
m = int(input())
for n in fibonacci(m):
    print(n)